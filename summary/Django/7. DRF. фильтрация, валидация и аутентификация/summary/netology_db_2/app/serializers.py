from rest_framework import serializers
from .models import Car


# ========================= ПРОДВИНУТЫЙ СЕРИАЛИЗАТОР (ModelSerializer) =============================
class CarSerializerFromModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'  # __all__ означает, что все поля будут обязательными. Мы могли бы прописать
        # только ('name',) - в таком случае у нас было бы только одно обязательное поле

    # ВНИМАНИЕ! Название валидирующей функции должно начинаться с validate_
    def validate_name(self, name: str) -> str:  # name - это значение, которое придет с фронтенда
        if len(name) < 3:
            # POST http://localhost:4000/api/v1/cars/ with body: {"name": "vv", "amount":  22}
            # Response will be: {"name": ["Car name must contains minimum 3 symbols"]}
            raise serializers.ValidationError('Car name must contains minimum 3 symbols')
        return name

    # ВНИМАНИЕ! Название данного сериализарора зарезервированно
    def validate(self, attrs):  # attrs - это словарь, где хранятся все значения, которые прилетят с фронтенда
        """
        Данный сериализатор используется для тех случаев, когда одно значение зависит от другого.
        """
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Password mismatch!')
        return attrs
    # POST http://localhost:4000/api/v1/cars/
    # with body: {"name": "Audi", "amount":  4, "password": "qwert", "password_confirm": "qwerty"}
    # Response will be: {"non_field_errors": ["Password mismatch!"]}
