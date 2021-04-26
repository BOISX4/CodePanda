from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.home_url = reverse('home')
		self.about_url = reverse('home-about')

	def test_home_GET(self):
		response = self.client.get(self.home_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'home/home.html')

	def test_about_GET(self):
		response = self.client.get(self.about_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'home/about.html')