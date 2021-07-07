from rest_framework import serializers


# Воспользуемся джанговским сериализатором для сериализации и десериализации.
# Для этого мы создадим собственный класс, наследуемый от rest_framework.serializers.Serializer
class CarSerializer(serializers.Serializer):
    # тут мы прописываем поля из модели Car и задаем им настройки преобразований
    id = serializers.IntegerField(read_only=True)  # read_only=True означает, что мы это поле не трогаем
    name = serializers.CharField()
