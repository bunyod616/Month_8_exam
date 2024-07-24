from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_user, name='login'),
    path('index', views.index, name='index'),
    path('filling/', views.filling, name='filling_money'),
    path('reports/', views.reports, name='reports'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('daily-stats/', views.daily_stats, name='daily_stats'),
    path('weekly-stats/', views.weekly_stats, name='weekly_stats'),
    path('monthly-stats/', views.monthly_stats, name='monthly_stats'),
]