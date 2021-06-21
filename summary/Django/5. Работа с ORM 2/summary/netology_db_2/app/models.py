from django.db import models


class CarShop(models.Model):
    """
    Модель Салон
    """
    name = models.CharField(verbose_name='Наименование магазина', max_length=254)
    # благодаря следующему полю у на с БД появится таблица app_carshop_car (m2m).
    # Аргумент related_name нужен для обратной связи. Тут в значении этого аргумента мы можем прописать любое слово,
    # главное, потом это слово прописать во view-функции, когда нам нужно будет получить данные через
    # обратную связь. Например: x = Car.objects.first().это_слово.all()
    # Аргумент elated_name должен быть прописан всегда.
    car = models.ManyToManyField('Car', related_name='shops')

    def __str__(self):
        return f'{self.id} - {self.name}'


class Car(models.Model):
    """
    Модель Машины
    """
    name = models.CharField(verbose_name='Наименование машины', max_length=254)

    def __str__(self):
        return f'{self.id} - {self.name}'
