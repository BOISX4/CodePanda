from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
# from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    question = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)
    user_ques = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    tags_ques = ArrayField(models.CharField(max_length=30), blank=True, null=True)
    def __str__(self):
        return self.title

class Answer(models.Model):
    answer = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)
    answer_for_ques = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_ans = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.answer