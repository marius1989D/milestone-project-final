from django.test import TestCase
from .forms import BugPostForm, BugCommentForm

class TestBugForms(TestCase):
	"""Test for Bug post forms"""
	def test_bug_form(self):
		form = BugPostForm({
			'title': 'abcd',
			'content': 'defghj'
		})
		print(form.errors)
		self.assertTrue(form.is_valid())

	"""Test for Bugs list view"""
	def test_get_bugs_page(self):
		page = self.client.get("/bugs/bugs_list/")
		self.assertEqual(page.status_code, 200)
		self.assertTemplateUsed(page, "bugs/bugs.html")