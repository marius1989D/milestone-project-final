from django.urls import path
from .views import bugs_list, bug_detail, bug_add, bug_delete, bug_edit

app_name = 'bugs'

urlpatterns = [
	path('bugs_list/', bugs_list, name='bugs_list'),
	path('<int:pk>/', bug_detail, name='bug_detail'),
	path('bug_add/', bug_add, name='bug_add'),
	path('<int:pk>/bug_delete/', bug_delete, name='bug_delete'),
	path('<int:pk>/bug_edit/', bug_edit, name='bug_edit'),
]