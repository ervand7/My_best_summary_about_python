from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app import api_view

router = DefaultRouter()
router.register('cars', api_view.CarViewSetVariant3, basename='cars')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls), name='cars')
]
