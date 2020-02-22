from django.test import TestCase

class TestCheckoutViews(TestCase):
	""" 
	Test the checkout view
	"""
	def test_cart_views_require_user_logged_in(self):
		checkout_page = self.client.get('/checkout/')

		self.assertEqual(checkout_page.status_code, 302)
		self.assertRedirects(checkout_page, '/accounts/login/?next=/checkout/')