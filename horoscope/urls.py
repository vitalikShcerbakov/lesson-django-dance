from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('type/', views.type),
    path('type/<element>', views.zodiac_element, name='type_name_element'),
    path('', views.index),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiak_by_numbers),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiak, name='horoscope-name'),
    ]