from django.contrib import admin
from django.urls import path
from app import api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_view.car_view, name='cars')
]
