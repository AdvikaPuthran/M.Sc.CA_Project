from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # Base URL will point to home page
]
