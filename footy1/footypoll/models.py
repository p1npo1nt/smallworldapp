from django.db import models
from django.forms import ModelForm

# Create your models here.

TEAM_NAMES = [
    'Arg',
    'Eng',
    'Liv',

]

class Players(models.Model):
    name = models.CharField(max_length=30)
    # team = models.CharField(max_length=3, choices=TEAM_NAMES)
    bd = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Stats(models.Model):
    goals_scored = models.IntegerField()
    starts = models.ManyToManyField(Players)

