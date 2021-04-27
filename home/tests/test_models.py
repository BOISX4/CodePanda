from django.test import TestCase
from home.models import Question, Answer
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
import datetime
class TestModels(TestCase):

	def setUp(self):

		self.user = User.objects.create_user(
			'user1',
			'user1@email.com',
			'user1password'
		)

		self.question1 = Question.objects.create(
			title = "Test 1",
    		question = "Test 1 question",
    		date_posted = '2021-11-11 10:30:40.12345644Z',
    		votes = 0,
    		user_ques = self.user,
    		tags_ques = ['array','dynamic']
    	)

	def test_question_url(self):
		self.assertEquals(self.question1.get_absolute_url(),'/question/1/')