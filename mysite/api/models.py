from django.db import models

class Senser(models.Model):
    x = models.FloatField(max_length=400)
    y = models.FloatField(max_length=400)
    z = models.FloatField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Senser2(models.Model):
    value = models.FloatField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
   return self.title