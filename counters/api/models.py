from django.db import models


class EnergyMeasurements(models.Model):
    number = models.IntegerField(
        'Номер счетчика',
        max_length=24
    )
    amps = models.FloatField(
        'Текущий ток (кол-во Ампер)',
        blank=True,
        null=True
    )
    kilowatt = models.FloatField(
        'Потребление энергии',
        blank=True,
        null=True
    )
    date = models.DateTimeField(
        'Время записи',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'показание'
        verbose_name_plural = 'показания'


class EnergyMeter(models.Model):
    number = models.IntegerField(
        'Номер счетчика',
        max_length=24,
        unique=True
    )

    class Meta:
        verbose_name = 'счетчик'
        verbose_name_plural = 'счетчики'
