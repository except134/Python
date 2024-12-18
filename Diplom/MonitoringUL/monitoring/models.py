from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return self.name

class INNList(models.Model):
    id = models.AutoField(primary_key=True)
    inn = models.CharField(max_length=16)
    pdffile = models.CharField(max_length=1024, blank=True)
    user = models.ManyToManyField(to=User, related_name="inns")

    def __str__(self):
        return self.inn

