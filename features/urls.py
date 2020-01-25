from django.urls import path

from .views import features_list, feature_detail, feature_add, feature_delete, feature_edit, feature_likes

app_name = 'features'

urlpatterns = [
	path('features_list/', features_list, name='features_list'),
	path('<int:pk>/', feature_detail, name='feature_detail'),
	path('feature_add/', feature_add, name='feature_add'),
	path('<int:pk>/feature_delete/', feature_delete, name='feature_delete'),
	path('<int:pk>/feature_edit/', feature_edit, name='feature_edit'),
	path('likes/<int:pk>/', feature_likes, name='feature_likes'),
]