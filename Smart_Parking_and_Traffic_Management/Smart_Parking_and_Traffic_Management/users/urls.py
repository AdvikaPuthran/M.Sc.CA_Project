from django.urls import path
from .views import register, user_login, user_logout, dashboard, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('signin/', user_login, name='signin'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('dashboard/', dashboard, name='dashboard'),
]
