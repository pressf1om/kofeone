from django.db import models

class Feedback(models.Model):
    email = models.CharField(max_length=100, verbose_name="Почта")
    text = models.TextField(verbose_name="Сообщение")

    def __str__(self):
        return self.name
