from django.db import models
from datetime import datetime


class Author(models.Model):
    name = models.CharField()
    age = models.IntegerField()
    created_at = models.DateField(default=datetime.now)
    status = models.BooleanField(default=False)


class Books(models.Model):
    name = models.CharField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.now)
    status = models.BooleanField(default=False)


class Order(models.Model):
    cust_name = models.CharField()
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    time = models.CharField()
    created_at = models.DateField(default=datetime.now)
    status = models.BooleanField(default=False)
