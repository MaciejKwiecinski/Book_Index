from django.db import models
from BookIndex.API.validators import PublishingValidator


class Book(models.Model):
    title = models.CharField(blank=False, max_length= 255)
    authors = models.CharField(blank=False, max_length= 255)
    published_date = models.IntegerField(validators=[PublishingValidator], blank=False)
    categories = models.CharField(blank=True, max_length= 255)
    average_rating = models.FloatField(blank=True)
    ratings_count = models.FloatField(blank=True)
    thumbnail = models.CharField(blank=True, max_length= 255)

    def __str__(self):
        return self.title

