from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Car
from .serializers import CarSerializerFromModelSerializer


# ВАРИАНТ 1. С ОПРЕДЕЛЕНИЕМ КЛАССА ФИЛЬТРАЦИИ
class CarFilter(filters.FilterSet):
    """
    Класс для определения фильтров. Тут мы прописываем возможные параметры для
    фильтрации под каждое поле модели.
    """
    # зададим 3 кастомных фильтра: id, amount_from и amount_to
    # http://127.0.0.1:4000/api/v1/cars/?id=3
    id = filters.ModelMultipleChoiceFilter(to_field_name="id", queryset=Car.objects.all())
    # http://127.0.0.1:4000/api/v1/cars/?amount_from=350
    amount_from = filters.NumberFilter(field_name="amount", lookup_expr="gte")  # lookup_expr - параметр фильтрации
    # http://127.0.0.1:4000/api/v1/cars/?amount_to=350
    amount_to = filters.NumberFilter(field_name="amount", lookup_expr="lte")

    class Meta:
        # тут мы должны заполнить 2 обязательных поля: model и fields
        model = Car
        fields = ("id", "amount_from", "amount_to",)


class CarViewSetVariant1(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializerFromModelSerializer
    # filter_backends, filterset_class - заразервирванные имена
    filter_backends = [DjangoFilterBackend]  # DjangoFilterBackend исполняет роль фильтрующего бекэнда
    filterset_class = CarFilter  # CarFilter - класс с прописанными фильтрами, который мы прописали выше


# ===============================================================================
# ВАРИАНТ 2. БЕЗ ОПРЕДЕЛЕНИЯ КЛАССА ФИЛЬТРАЦИИ

class CarViewSetVariant2(viewsets.ModelViewSet):
    """
    https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html#using-the-filterset-fields-shortcut
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializerFromModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'amount']
    # http://127.0.0.1:4000/api/v1/cars/?name=first_car
    # http://127.0.0.1:4000/api/v1/cars/?amount=300


# ===============================================================================
# ВАРИАНТ 3. БЕЗ ИСПОЛЬЗОВАНИЯ БИБЛИОТЕКИ django_filters. ПОЛНОСТЬЮ КАСТОМНЫЙ ПУТЬ

class CarViewSetVariant3(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializerFromModelSerializer
    # filter_backends, filterset_fields - зарезервированные имена
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'amount']

    def get_queryset(self):
        """
        Переопределяем get_queryset родительского класса.
        """
        queryset = super().get_queryset()
        amount = self.request.query_params.get('amount')
        if amount:
            queryset = queryset.filter(amount=amount)
        # http://127.0.0.1:4000/api/v1/cars/?amount=2
        return queryset
