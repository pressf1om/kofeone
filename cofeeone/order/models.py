from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена")
    quantity = models.IntegerField(verbose_name="Остаток")

    def __str__(self):
        return self.name