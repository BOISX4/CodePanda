from django.test import SimpleTestCase
from django.urls import reverse,resolve
from home.views import QuestionListView,QuestionDetailView,QuestionUpdateView,QuestionDeleteView,QuestionCreateView,about

class TestUrls(SimpleTestCase):

	def test_home_url_resolves(self):
		url = reverse('home')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,QuestionListView)

	def test_question_detail_url_resolves(self):
		url = reverse('question-detail',args=[1])
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,QuestionDetailView)

	def test_question_update_url_resolves(self):
		url = reverse('question-update',args = [1])
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,QuestionUpdateView)

	def test_question_delete_url_resolves(self):
		url = reverse('question-delete',args = [1])
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,QuestionDeleteView)

	def test_question_create_url_resolves(self):
		url = reverse('question-create')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,QuestionCreateView)
		
	def test_about_url_resolves(self):
		url = reverse('home-about')
		print(resolve(url))
		self.assertEquals(resolve(url).func,about)