from django.db import models


class Player(models.Model):  # обязательное наследование
    # Мы можем не указывать первичный ключ у этой модели. По умолчанию Django создает его
    # Если же мы все таки хотим задать свой первичный ключ, то это делается так:
    address = models.TextField(primary_key=True)

    # значения полей тоже должны браться из models
    name = models.TextField()
