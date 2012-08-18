from django.db import models

from bobvillewiki.player.models import Player

class SentenceType(models.model):
    type = models.CharField(max_length=24)

class TimeUnit(models.model):
    unit = models.CharField(max_length=24)

class Sentence(models.model):
    type = models.ForeignKey(SentenceType)
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    units = models.ForeignKey(TimeUnits)

class Violation(models.model):
    violator = models.ForeignKey(Player)
    victim = models.ForeignKey(Player)
    sentence = models.ForeignKey(Sentence)
    note = models.TextField(max_length=5000)
    sentence_complete = models.BooleanField(default=False)