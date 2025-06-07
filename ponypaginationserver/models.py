from django.db import models


class Pony(models.Model):
    name = models.CharField(max_length=255)
    is_available = models.BooleanField()
