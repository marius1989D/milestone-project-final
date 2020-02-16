from django.test import TestCase
from .forms import CommentForm

class TestBlogCommentForm(TestCase):

	"""Test blog-post comment form"""
	def test_comment_form(self):
		form = CommentForm({
			'name': 'abcd', 
			'email': 'abcd@789.ro', 
			'body': 'comment'
		})
		self.assertTrue(form.is_valid())


	"""Test for blog-post views"""
	def test_blog_posts_home_page(self):
		page = self.client.get("/blog/")
		self.assertEqual(page.status_code, 200)
		self.assertTemplateUsed(page, "blog/post_list.html")
