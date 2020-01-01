from django.urls import path
from .views import bugs_list, bug_detail, bug_add

urlpatterns = [
	path('', bugs_list, name='bug_list'),
	path('bug_detail/<pk>/', bug_detail, name='bug_detail'),
	path('bug_add', bug_add, name='bug_add'),
]