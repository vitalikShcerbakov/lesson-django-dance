from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

dict_signs_zodiak = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}


def index(request):
    zodiac = list(dict_signs_zodiak)
    li_elements = ''
    for sign in zodiac:
        redirect_path = reverse('horoscope-name', args=(sign,))
        li_elements += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
    respone = f"""
    <ul>
        {li_elements} 
    </ul>"""
    return HttpResponse(respone)


# Create your views here.
def get_info_about_sign_zodiak(request, sign_zodiac: str):
    discription = dict_signs_zodiak.get(sign_zodiac)
    if discription:
        return HttpResponse(discription)
    else:
        return HttpResponseNotFound(f"Вы что то напутали, {sign_zodiac} не существует")


def get_info_about_sign_zodiak_by_numbers(request, sign_zodiac: int):
    zodiac = list(dict_signs_zodiak)
    if sign_zodiac > len(zodiac):
        return HttpResponseNotFound(f"очень большой индекс, {sign_zodiac}  знаков задиака не существует")
    name_zodiac = zodiac[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)
