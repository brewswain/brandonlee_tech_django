"""Defines URLs patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'portfolio_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index')
]