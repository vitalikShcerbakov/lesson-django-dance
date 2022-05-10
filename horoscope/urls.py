from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiak_by_numbers),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiak, name='horoscope-name'),
    ]