from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Question
from .models import Answer
from django.contrib.auth.mixins import LoginRequiredMixin
#  UserPassesTestMixin

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
    fields =['title', 'question']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    fields =['title', 'question']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
     
    # def test_func(self):
    #     question = self.get_object()
    #     if self.request.user == question.user_ques:
    #         return True
    #     return False

# class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Question

#     def test_func(self):
#         question = self.get_object()
#         if self.request.user == question.user_ques:
#             return True
#         return False

def about(request):
    return render(request, 'home/about.html', {'title': 'about'})

# UserPassesTestMixin