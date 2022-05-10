from django.urls import path
from . import views

urlpatterns = [
    path('<int:day>/', views.day_of_the_week_int),
    path('<day>/', views.day_of_the_week, name='day_name'),

]
