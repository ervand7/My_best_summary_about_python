from django.db import models


class Project(models.Model):
    """Объект на котором проводят измерения."""

    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объект на карте'
        verbose_name_plural = 'Объекты на карте'


class Measurement(models.Model):
    """Измерение температуры на объекте."""

    value = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True  # автоматическое проставление даты при создании
    )
    updated_at = models.DateTimeField(
        auto_now=True  # автоматическое проставление даты при обновлении
    )

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Результат измерения'
        verbose_name_plural = 'Результаты измерения'
