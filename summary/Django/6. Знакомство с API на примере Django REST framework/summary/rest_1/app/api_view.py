from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Car

GET = 'GET'
POST = 'POST'
METHODS = [GET, POST]


def car_view(request):
    # мы сейчас хотим, чтобы эта вьюха работала по ресту и обрабатывала запросы
    # поэтому мы проверяем достоверность методов, которые к нам пришли
    if request.method not in METHODS:
        return HttpResponse(status=405)
        # Код 405 Method Not Allowed говорит нам о том, что сервер получил определенный
        # запрос с заданным HTTP-методом, смог его распознать, но не дает добро на его
        # реализацию. То есть пользователь не получит доступ к контенту, который запросил.
    if request.method == GET:
        cars = Car.objects.all()
        dat = [{'id': car.id, 'name': car.name} for car in cars]
        data = {{'id': car.id, 'name': car.name} for car in cars}
        print('====>', data)
        # здесь можно было бы использовать стандартный json.dumps()
        # но мы будем использовать джанговский метод JsonResponse
        return JsonResponse(dat, safe=False, status=200)

