from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm

class TestAccountsForms(TestCase):
	"""Tests for login and registration forms"""
	def test_login_form(self):
		form = UserLoginForm({
			'username_or_email': 'abcd',
			'password': 'marius123A'
		})
		print(form.errors)
		self.assertTrue(form.is_valid())

	def test_registration_form(self):
		form = UserRegistrationForm({
			'username': 'abcd',
			'email': 'abcd@789.ro',
			'password1': 'marius123A',
			'password2': 'marius123A'
		})
		self.assertTrue(form.is_valid())

	
