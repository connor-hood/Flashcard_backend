from django.db import models


# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=30)


class Card(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    card_count = models.IntegerField()

