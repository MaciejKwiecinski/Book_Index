from django.db import models

class Author(models.Model):
    name = models.CharField(blank=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(blank=False)
    authors = models.ManyToManyField(Author, through="Author_book", on_delete=models.CASCADE)
    published_date = models.CharField(blank=False)
    categories = models.CharField(blank=True)
    average_rating = models.FloatField(blank=True)
    ratings_count = models.FloatField(blank=True)
    thumbnail = models.CharField(blank=True)

class Author_book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

