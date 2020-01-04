from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User






class Bug(models.Model):

	"""
	Creates a bug post model on the database
	"""

	Received = 'Received'
	In_progress = 'In progress'
	Done = 'Done'

	CHOICES = [
		(Received, 'Received'),
		(In_progress, 'In progress'),
		(Done, 'Done')
	]

	title = models.CharField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=15 ,choices=CHOICES, default=Received)
	views = models.IntegerField(default=0)

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title
	
class Comment(models.Model):
	bug = models.ForeignKey(Bug, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)

	class Meta:
		ordering = ['created_on']

	def __str__(self):
		return 'Comment {} by {}'.format(self.body, self.name)



