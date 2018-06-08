from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=140)
    author = models.CharField(max_length=140)
    publication_date = models.DateTimeField()