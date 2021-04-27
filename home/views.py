from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Question
from .models import Answer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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

