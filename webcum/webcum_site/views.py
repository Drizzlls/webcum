from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.mail import send_mail
import requests

def index(request):
    return render(request, 'webcum_site/index.html')


def treatment(request):
    if request.method == "POST":
        dataArtem = f'Пришел новый лид с сайта!\nИмя: {request.POST.get("name", "ошибка")}\nТелефон: {request.POST.get("phone", "ошибка")}'
        dataVika = f'Пришел новый лид с сайта!\nИмя: {request.POST.get("name", "ошибка")}\nТелефон: {request.POST.get("phone", "ошибка")}'
        dataRuslan = f'Пришел новый лид с сайта!\nИмя: {request.POST.get("name", "ошибка")}\nТелефон: {request.POST.get("phone", "ошибка")}'
        req = requests.get(
            f'https://api.telegram.org/bot6570350252:AAFqKIDV7frgQ6MEWiB0cRFmpkJJuuXRWBA/sendMessage?chat_id=392948054&text={dataArtem}')
        req = requests.get(
            f'https://api.telegram.org/bot6570350252:AAFqKIDV7frgQ6MEWiB0cRFmpkJJuuXRWBA/sendMessage?chat_id=585753600&text={dataVika}')
        req = requests.get(
            f'https://api.telegram.org/bot6570350252:AAFqKIDV7frgQ6MEWiB0cRFmpkJJuuXRWBA/sendMessage?chat_id=272635960&text={dataRuslan}')
    return HttpResponse(True)