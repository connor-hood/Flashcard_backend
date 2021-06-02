from django.db import models


# Create your models here.
class Card(models.Model):
    language = models.CharField(max_length=20)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    card_count = models.IntegerField()
