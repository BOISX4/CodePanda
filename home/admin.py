from django.contrib import admin
from .models import Question, Answer, VoteAnswer, VoteQuestion

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(VoteQuestion)
admin.site.register(VoteAnswer)