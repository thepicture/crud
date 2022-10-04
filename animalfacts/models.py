from django.db import models
from django.db.models import Avg


class Breed(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.title


class AnimalFact(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, blank=True)
    fact = models.CharField(max_length=512)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    image = models.ImageField(null=True)

    def __str__(self) -> str:
        return self.title + ', ' + self.breed.title
