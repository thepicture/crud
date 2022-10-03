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

    def average_rating(self):
        ratings = Rating.objects.filter(animal_fact_id=self.id)
        if not len(ratings):
            return 0
        else:
            return ratings.aggregate(Avg('count_of_stars'))['count_of_stars__avg']

    def rating_as_stars(self):
        rating = round(self.average_rating())
        return '\u2605' * (rating) + '\u2730' * (5 - rating)

    def __str__(self) -> str:
        return self.title + ', ' + self.breed.title


class Rating(models.Model):
    count_of_stars = models.IntegerField()
    animal_fact = models.ForeignKey(
        AnimalFact, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.animal_fact.title + ', stars: ' + str(self.count_of_stars)
