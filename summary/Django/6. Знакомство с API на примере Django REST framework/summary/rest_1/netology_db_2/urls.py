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
    path('api/v1/cars/', api_view.car_view, name='cars')
]
