from django.db import models


class EnergyMeasurements(models.Model):
    number = models.CharField(
        'Номер счетчика',
        max_length=24,
        primary_key=True
    )
    amps = models.CharField(
        'Текущий ток (кол-во Ампер)',
        blank=True,
        null=True
    )
    kilowatt = models.CharField(
        'Потребление энергии',
        blank=True,
        null=True
    )
    date = models.DateTimeField(
        'Время записи',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'счетчик'
        verbose_name_plural = 'счетчики'


class EnergyMeter(models.Model):
    number = models.ForeignKey(
        EnergyMeasurements,
        on_delete=models.CASCADE
    )
    amps = models.CharField(
        'Текущий ток (кол-во Ампер)',
        blank=True,
        null=True
    )
    kilowatt = models.CharField(
        'Потребление энергии',
        blank=True,
        null=True
    )
