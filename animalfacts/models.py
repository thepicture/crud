from django.db import models
from django.db.models import Avg

from django.contrib.contenttypes.fields import GenericRelation

from star_ratings.models import Rating

from chartjs.views.lines import BaseLineChartView


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

    ratings = GenericRelation(Rating, related_query_name='ratings')

    def __str__(self) -> str:
        return self.title + ', ' + self.breed.title

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return labels for the x-axis."""
        return [f.title for f in AnimalFact.objects.all()]

    def get_providers(self):
        """Return names of datasets."""
        return ["Stars"]

    def get_data(self):
        """Return dataset to plot."""
        return [[f.ratings.all()[0].average for f in AnimalFact.objects.all()] * AnimalFact.objects.count()]