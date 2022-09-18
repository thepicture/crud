from django.db import models
from django.db.models import Avg


class Breed(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.title


class AnimalFact(models.Model):
    title = models.CharField(max_length=64, null=False)
    description = models.CharField(max_length=1024, blank=True)
    fact = models.CharField(max_length=512, null=False)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, null=False)

    def average_rating(self):
        return Rating.objects \
            .filter(animal_fact_id=self.id) \
            .aggregate(Avg('count_of_stars'))['count_of_stars__avg']

    def __str__(self) -> str:
        return self.title + ', ' + self.breed.title


class Rating(models.Model):
    count_of_stars = models.IntegerField(null=False)
    animal_fact = models.ForeignKey(
        AnimalFact, on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return self.animal_fact.title + ', stars: ' + str(self.count_of_stars)
