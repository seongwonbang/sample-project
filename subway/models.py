from django.db import models


# Create your models here.

class Station(models.Model):
    name = models.CharField(max_length=20, null=False, primary_key=True)

    def __str__(self):
        return self.name


class Line(models.Model):
    name = models.CharField(max_length=20, null=False, primary_key=True)
    stations = models.ManyToManyField(Station, related_name='lines')
