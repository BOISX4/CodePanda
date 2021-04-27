from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Profile

class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.register_url = reverse('register')
		self.profile_url = reverse('profile')
		self.client.force_login(User.objects.get_or_create(username='testuser')[0])

	def test_register_POST_valid_form(self):

		response = self.client.post(self.register_url, {
			'username' : 'user1',
			'email' : 'user1@email.com',
			'password1' : 'user1password',
			'password2' : 'user1password'
			})
		self.assertEquals(response.status_code, 302)

	def test_register_POST_invalid_form(self):

		response = self.client.post(self.register_url, {
			'username' : 'user1',
			'email' : '',
			'password1' : 'user1password',
			'password2' : 'user1password'
			})
		self.assertTemplateUsed(response, 'users/register.html')

	def test_register_form_GET(self):
		response = self.client.get(self.register_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'users/register.html')

	def test_profile_POST_valid(self):

		response = self.client.post(self.profile_url, {
			'username':'user11',
			'email': 'user11@email.com'
			})
		self.assertEquals(response.status_code, 302)
		
	def test_profile_POST_invalid(self):

		response = self.client.post(self.profile_url, {
			'username':'user11',
			'email': ''
			})
		self.assertTemplateUsed(response, 'users/profile.html')

	def test_profile_form_GET(self):
		response = self.client.get(self.profile_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'users/profile.html')