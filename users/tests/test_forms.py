from django.test import TestCase
from django.contrib.auth.models import User
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm 
class TestForms(TestCase):

	def test_user_register_form_valid(self):
		form = UserRegisterForm(
			data = {
			'username' :"user2",
			'email' : "user2@email.com",
			'password1' : "user2password",
			'password2' : "user2password"
			}
		)

		self.assertTrue(form.is_valid())
	def test_user_register_form_invalid(self):
		form = UserRegisterForm(
			data = {
			'username' :"user2",
			'email' : "",
			'password1' : "user1password",
			'password2' : "user2password"
			}
		)

		self.assertFalse(form.is_valid())
		
	def test_user_update_form_valid(self):
		form = UserUpdateForm(
			data = {
			'username' :"user2",
			'email' : "user2@email.com"
			}
		)

		self.assertTrue(form.is_valid())
	def test_user_update_form_invalid(self):
		form = UserUpdateForm(
			data = {
			'username' :"user2",
			'email' : ""
			}
		)

		self.assertFalse(form.is_valid())
	def test_user_profile_update_form_invalid(self):
		form = UserUpdateForm(
			data = {
			'image' :""
			}
		)

		self.assertFalse(form.is_valid())