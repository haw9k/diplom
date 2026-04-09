from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('stats/', views.stats_view, name='stats'),
    path('achievements/', views.achievements_view, name='achievements'),
    path('users/', views.users_view, name='users'),
    path('system-users/', views.system_users_view, name='system_users'),
]
