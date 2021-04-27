from django.test import SimpleTestCase
from django.urls import reverse,resolve
from users.views import register, profile
from django.contrib.auth.views import LoginView, LogoutView
class TestUrls(SimpleTestCase):

	def test_register_url_resolves(self):
		url = reverse('register')
		print(resolve(url))
		self.assertEquals(resolve(url).func,register)

	def test_profile_url_resolves(self):
		url = reverse('profile')
		print(resolve(url))
		self.assertEquals(resolve(url).func,profile)

	def test_login_url_resolves(self):
		url = reverse('login')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,LoginView)

	def test_logout_url_resolves(self):
		url = reverse('logout')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,LogoutView)