from django.db import models

from apps.car.models import Car


class Maintenance(models.Model):
    mileage = models.PositiveSmallIntegerField(verbose_name='Kilometraje')
    description = models.CharField(max_length=200, verbose_name='Descripcion')
    cost = models.PositiveIntegerField(verbose_name='Costo')
    date = models.DateTimeField(verbose_name='Fecha')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'

    def __str__(self):
        return '%s %s %s %s' % (self.car, self.description, self.date, self.cost)

