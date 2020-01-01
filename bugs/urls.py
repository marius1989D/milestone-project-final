from django.urls import path
from . import views

urlpatterns = [
	path('', views.BugList.as_view(), name='bug_list')
]