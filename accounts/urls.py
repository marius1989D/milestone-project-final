from . import views
from .views import index, registration
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('register/', registration, name='register'),
]