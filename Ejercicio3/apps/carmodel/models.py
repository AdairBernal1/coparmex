from django.db import models

from apps.brand.models import Brand


class Carmodel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Modelo')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def __str__(self):
        return '%s %s' % (self.brand, self.name)
