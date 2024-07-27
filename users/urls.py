"""Defines URL patterns for users"""

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'

urlpatterns = [
    # Login Page.
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    # Registration page
    path('register/', views.register, name='register'),

    # Logout Page.
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
]