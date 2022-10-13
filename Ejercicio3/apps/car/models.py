from django.db import models

from apps.user.models import User

from apps.carmodel.models import Carmodel


class Car(models.Model):
    plate = models.CharField(max_length=20, verbose_name='Placa')
    mileage = models.PositiveSmallIntegerField(verbose_name='Kilometraje')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carmodel = models.ForeignKey(Carmodel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Automovil'
        verbose_name_plural = 'Automoviles'

    def __str__(self):
        return '%s %s %s' % (self.carmodel, self.plate, self.user)
