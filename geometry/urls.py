from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('get_rectangle_area/<int:width>/<int:height>', views.rectangle),
    path('get_square_area/<int:width>', views.square),
    path('get_circle_area/<int:radius>', views.circle),

    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area, name='rectangle_name'),
    path('square/<int:width>', views.get_square_area, name='square_name'),
    path('circle/<int:radius>', views.get_circle_area, name='circle_name'),
]
