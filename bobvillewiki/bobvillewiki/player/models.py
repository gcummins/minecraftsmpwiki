from django.db import models

class Rank(models.Model):
    rank = models.CharField(max_length=24)

class Player(models.Model):
    username = models.CharField(max_length=50)
    website_username = models.CharField(max_length=50)
    rank = models.ForeignKey(Rank)
