from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400, default="This is a product")
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083, default="This is an image")


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

