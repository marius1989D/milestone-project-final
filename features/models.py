from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User






class Feature(models.Model):

	"""
	Creates a Feature post model on the database
	"""

	Received = 'Received'
	In_progress = 'In progress'
	Done = 'Done'

	CHOICES = [
		(Received, 'Received'),
		(In_progress, 'In progress'),
		(Done, 'Done')
	]

	title = models.CharField(max_length=200, unique=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feature_report')
	content = models.TextField()
	likes = models.IntegerField(default=0)
	created_on = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=15 ,choices=CHOICES, default=Received)
	views = models.IntegerField(default=0)
	price = models.DecimalField(max_digits=6, decimal_places=2, default=10, null=True, blank=True)


	class Meta:
		ordering = ['-created_on']

	def get_absolute_url(self):
		return "features/%d/%s"%(self.id, self.title)

	def __str__(self):
		return self.title

	
class Comment(models.Model):
	"""
	Creates a comment model on the database
	"""
	feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)

	class Meta:
		ordering = ['created_on']

	def __str__(self):
		return 'Comment {} by {}'.format(self.body, self.name)

class Contribution(models.Model):
	"""
	Creates a contribution model on the database
	"""
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	feature = models.ForeignKey(Feature, on_delete=models.DO_NOTHING)
	amount = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
	contributed_on = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.author.username



