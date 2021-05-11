from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, Http404
from .models import Question
from django.http import HttpResponse
from .models import Question, VoteQuestion
from .models import Answer, VoteAnswer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import F
from django.db.models import Q
from django.http import JsonResponse
from .forms import AnswerForm


def search_title(request):
    if request.method == "POST":
        searched = request.POST['searched']
        questions = Question.objects.filter(title__contains=searched )
        return render(request, 'home/search_title.html', {'searched': searched,'questions':questions})
    else:
        return render(request, 'home/search_title.html', {})

def home(request):
    context = {
        'questions': Question.objects.all()
    }
    return render(request, 'home/home.html', context)


class QuestionListView(ListView):
    model = Question
    template_name ='home/home.html'
    context_object_name = 'questions'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Question
    template_name ='home/user_posts.html'
    context_object_name = 'questions'
    # queryset = Question.objects.filter(user_ques_id=1).order_by('-date_posted')
    paginate_by = 5

    def get_queryset(self):
        userid = self.request.user.id
        # User.objects.get(username=the_username).pk
        return Question.objects.filter(user_ques=userid).order_by('-date_posted')

class PandaProfileView(ListView):
    model = Question
    template_name ='home/panda_profile.html'
    context_object_name = 'questions'
    # queryset = Question.objects.filter(user_ques_id=1).order_by('-date_posted')
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        userid = self.request.user.id
        # User.objects.get(username=the_username).pk
        return Question.objects.filter(user_ques=self.kwargs['pk']).order_by('-date_posted')


class QuestionDetailView(DetailView):
    model = Question

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields =['title', 'question', 'tags_ques']

    def form_valid(self, form):
        form.instance.user_ques = self.request.user
        return super().form_valid(form)

class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields =['title', 'question', 'tags_ques']

    def form_valid(self, form):
        form.instance.user_ques = self.request.user
        return super().form_valid(form)
     
    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user_ques:
            return True
        return False

class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    success_url = '/'

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user_ques:
            return True
        return False


def about(request):
    return render(request, 'home/about.html', {'title': 'about'})

def voteans(request):
    
    if request.POST.get('action') == 'votes':

        id = int(request.POST.get('answerid'))
        button = request.POST.get('button')
        update = Answer.objects.get(id=id)

        print(id)

        # Check if user has voted already
        if update.vote_ans.filter(id=request.user.id).exists():

            # Get user current vote
            q = VoteAnswer.objects.get(Q(answer_id=id) & Q(user_id=request.user.id))
            evote = q.vote

            if evote == True:

                # User clicks upvote again, remove vote
                if button == 'upvote':
                    update.votes = F('votes') - 1
                    update.vote_ans.remove(request.user)
                    update.save()
                    update.refresh_from_db()
                    votes = update.votes
                    q.delete()
                    
                    return JsonResponse({'votes': votes})

                if button == 'downvote':
                    update.votes = F('votes') - 2
                    update.save()
                    q.vote = False
                    q.save(update_fields=['vote'])
                    update.refresh_from_db()
                    votes = update.votes


                    return JsonResponse({'votes': votes})

            pass 

            if evote == False:

                # User clicks downvote again, remove vote
                if button == 'downvote':
                    update.votes = F('votes') + 1
                    update.vote_ans.remove(request.user)
                    update.save()
                    update.refresh_from_db()
                    votes = update.votes
                    q.delete()
                    
                    return JsonResponse({'votes': votes})

                if button == 'upvote':
                    update.votes = F('votes') + 2
                    update.save()
                    q.vote = True
                    q.save(update_fields=['vote'])
                    update.refresh_from_db()
                    votes = update.votes
                    
                    return JsonResponse({'votes': votes})

        else:

            if button == 'upvote':
                update.votes = F('votes') + 1
                update.vote_ans.add(request.user)
                update.save()

                new = VoteAnswer(answer_id=id, user_id=request.user.id, vote=True)
                new.save()
            else:
                update.votes = F('votes') - 1
                update.vote_ans.add(request.user)
                update.save()

                new = VoteAnswer(answer_id=id, user_id=request.user.id, vote=False)
                new.save()

            update.refresh_from_db()
            votes = update.votes

            return JsonResponse({'votes': votes})

    pass

def voteques(request):
    
    if request.POST.get('action') == 'votes':

        id = int(request.POST.get('questionid'))
        button = request.POST.get('button')
        update = Question.objects.get(id=id)

        # Check if user has voted already
        if update.vote_ques.filter(id=request.user.id).exists():

            # Get user current vote
            q = VoteQuestion.objects.get(Q(question_id=id) & Q(user_id=request.user.id))
            evote = q.vote

            if evote == True:

                # User clicks upvote again, remove vote
                if button == 'upvote':
                    update.votes = F('votes') - 1
                    update.vote_ques.remove(request.user)
                    update.save()
                    update.refresh_from_db()
                    votes = update.votes
                    q.delete()
                    
                    return JsonResponse({'votes': votes})

                if button == 'downvote':
                    update.votes = F('votes') - 2
                    update.save()
                    q.vote = False
                    q.save(update_fields=['vote'])
                    update.refresh_from_db()
                    votes = update.votes


                    return JsonResponse({'votes': votes})

            pass 

            if evote == False:

                # User clicks downvote again, remove vote
                if button == 'downvote':
                    update.votes = F('votes') + 1
                    update.vote_ques.remove(request.user)
                    update.save()
                    update.refresh_from_db()
                    votes = update.votes
                    q.delete()
                    
                    return JsonResponse({'votes': votes})

                if button == 'upvote':
                    update.votes = F('votes') + 2
                    update.save()
                    q.vote = True
                    q.save(update_fields=['vote'])
                    update.refresh_from_db()
                    votes = update.votes
                    
                    return JsonResponse({'votes': votes})

        else:

            if button == 'upvote':
                update.votes = F('votes') + 1
                update.vote_ques.add(request.user)
                update.save()

                new = VoteQuestion(question_id=id, user_id=request.user.id, vote=True)
                new.save()
            else:
                update.votes = F('votes') - 1
                update.vote_ques.add(request.user)
                update.save()

                new = VoteQuestion(question_id=id, user_id=request.user.id, vote=False)
                new.save()

            update.refresh_from_db()
            votes = update.votes

            return JsonResponse({'votes': votes})

    pass