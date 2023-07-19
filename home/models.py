from typing import Any
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    email =models.EmailField()


    def __str__(self):
        return self.name