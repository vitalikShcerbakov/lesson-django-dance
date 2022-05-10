from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def get_rectangle_area(request, width, height):
    return HttpResponse(f"Площадь прямоугольника размером {width} x {height} равна {width * height}")


def get_square_area(request, width):
    return HttpResponse(f"Площадь квадрата равна {width * width}")


def get_circle_area(request, radius):
    return HttpResponse(f"Площадь круга равна {3.14 * (radius ** 2)}")




def rectangle(request, width, height):
    redirect_url = reverse('rectangle_name', args=((width*height), ))
    return HttpResponseRedirect(redirect_url)


def square(request, width):
    redirect_url = reverse('square_name', args=(width,))
    return HttpResponseRedirect(redirect_url)


def circle(request, radius):
    redirect_url = reverse('square_name', args=(radius,))
    return HttpResponseRedirect(redirect_url)

