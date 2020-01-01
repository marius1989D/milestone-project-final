from django.urls import path
from . import views

urlpatterns = [
	path('', views.BugList.as_view(), name='bugs_home')
]