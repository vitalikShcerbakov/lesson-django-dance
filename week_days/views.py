from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
dict_days = {
    'monday': "Убрать дома",
    'tuesday': 'сходить за водой',
    'wednesday': 'приготовить обед',
    'thursday': 'сделать уроки',
    'friday': 'напится))',
    'saturday': 'заменить водительский права',
    'sunday': 'отдыхаем весь день'
}
def day_of_the_week(request, day):

    if day in dict_days:
        return HttpResponse(f'В {day} этот день надо {dict_days[day]}')
    else:
        return HttpResponseNotFound(f"{day} не день недели")

def day_of_the_week_int(request, day):
    if 1 <= day <= 7:
        list_days = list(dict_days)
        day_week = list_days[day-1]
        redirect_url = reverse('day_name', args=(day_week, ))
        return HttpResponseRedirect(redirect_url)

    return HttpResponseNotFound(f"Как то  {day} много для дней в недели, их то всего 7 =)")