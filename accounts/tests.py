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

	"""Tests for login and registration views"""
	def test_get_login_page(self):
		page = self.client.get("/accounts/login/")
		self.assertEqual(page.status_code, 200)
		self.assertTemplateUsed(page, "accounts/login.html")

	def test_get_registration_page(self):
		page = self.client.get("/accounts/register/")
		self.assertEqual(page.status_code, 200)
		self.assertTemplateUsed(page, "accounts/register.html")
