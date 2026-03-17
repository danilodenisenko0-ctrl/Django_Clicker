# game/models.py
from django.db import models

class Upgrade(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=10)
    clicks_per_second = models.IntegerField(default=1)  # необов’язково, якщо хочеш авто-кліки

    def __str__(self):
        return self.name