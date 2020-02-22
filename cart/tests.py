from django.test import TestCase
from .views import view_cart, add_to_cart, adjust_cart

class TestCartViews(TestCase):
	"""
	Tests the cart app views requires user to be logged in
	"""
	def test_cart_views_require_user_logged_in(self):
		cart_page = self.client.get('/cart/')
		cart_add = self.client.get('/cart/1/add/')
		cart_update = self.client.get('/cart/1/adjust')

		self.assertEqual(cart_page.status_code, 302)
		self.assertEqual(cart_add.status_code, 302)
		self.assertEqual(cart_update.status_code, 301)

		self.assertRedirects(cart_page, '/accounts/login/?next=/cart/')


