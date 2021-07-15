"""
Program to define model of Books Details
Edited By: Rushabh Pancholi
"""

from django.db import models
from authors.models import Author

# Create your models here.


class Book(models.Model):
    name = models.TextField(max_length=256)
    isbn = models.TextField(max_length=13)
    author = models.ForeignKey(
        Author, null=True, related_name='author', on_delete=models.SET_NULL)

    def __str__(self):
        return '%s %s %s' % (self.name, self.isbn, self.author)
