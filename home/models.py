from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    question = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)
    # user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class Answer(models.Model):
    answer = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)
    answer_for_ques = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer