from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    age = models.PositiveIntegerField(validators=[
            MaxValueValidator(150),
            MinValueValidator(14)
        ])
    password = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=1024, blank=True)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(to=Buyer)

    def __str__(self):
        return self.title
