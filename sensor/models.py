from django.db import models


class Sensor(models.Model):
    Action = models.CharField(max_length=400)
    DeviceName = models.CharField(max_length=400)
    SensorName = models.CharField(max_length=400)
    X = models.FloatField(max_length=400)
    Y = models.FloatField(max_length=400)
    Z = models.FloatField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.title
