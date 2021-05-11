from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse


# Create your models here.
class Question(models.Model):
    
    title = models.CharField(max_length=100)
    question = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)
    vote_ques = models.ManyToManyField(User, related_name='vote_ques', default=None, blank=True)
    user_ques = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    tags_ques = ArrayField(models.CharField(max_length=30), blank=True, null=True, verbose_name='Tags for Question')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question-detail', kwargs={'pk': self.pk})


class Answer(models.Model):
    answer_for_ques = models.ForeignKey(Question, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    answer = models.TextField()
    votes = models.IntegerField(default=0)
    vote_ans = models.ManyToManyField(User, related_name='vote_ans', default=None, blank=True)
    user_ans = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.answer


class VoteAnswer(models.Model):
    answer = models.ForeignKey(Answer, related_name='answerid', on_delete=models.CASCADE, default=None, blank=True)
    user = models.ForeignKey(User, related_name='userid', on_delete=models.CASCADE, default=None, blank=True)
    vote = models.BooleanField(default=True)


class VoteQuestion(models.Model):
    question = models.ForeignKey(Question, related_name='questionid', on_delete=models.CASCADE, default=None, blank=True)
    user = models.ForeignKey(User, related_name='userid1', on_delete=models.CASCADE, default=None, blank=True)
    vote = models.BooleanField(default=True)