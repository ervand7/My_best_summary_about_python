from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from app import api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # правило написания урлов в API: api/версия/endpoint
    # Внимание! Чтобы сейчас (без использования DRF) отправить POST-запрос и не получить ошибку 403,
    # мы должны отключить проверку на наличие CSRF-токена (прав на отправку этого запроса)
    # path('api/v1/cars/', csrf_exempt(api_view.car_view), name='cars')

    # далее по лекции нам уже не нужно использовать csrf_exempt
    # path('api/v1/cars/', api_view.car_view, name='cars'),

    # РЕАЛИЗАЦИЯ VIEWS НА ОСНОВЕ КЛАССОВ
    path('api/v1/cars/', api_view.CarApiView.as_view(), name='cars')
]
