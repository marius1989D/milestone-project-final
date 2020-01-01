from django.shortcuts import render
from django.views import generic
from .models import Bug

# Create your views here.
class BugList(generic.ListView):
	

	"""
	This view will list all bugs 
	"""
	queryset = Bug.objects.order_by('created_on').all()
	template_name = 'bugs/bugs.html'
	paginate_by = 3

	