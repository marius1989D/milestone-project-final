from django.test import TestCase
from .forms import FeaturePostForm, FeatureCommentForm

class TestFeatureForms(TestCase):
	"""Test for Feature post forms"""
	def test_bug_form(self):
		form = FeaturePostForm({
			'title': 'abcd',
			'content': 'defghj'
		})
		print(form.errors)
		self.assertTrue(form.is_valid())

	"""Test for Features list view"""
	def test_get_features_page(self):
		page = self.client.get("/features/features_list/")
		self.assertEqual(page.status_code, 200)
		self.assertTemplateUsed(page, "features/features.html")
