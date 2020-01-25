from django.urls import path, include
from . import urls_reset
from .views import index, register, logout, login

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('password-reset/', include(urls_reset)),
]