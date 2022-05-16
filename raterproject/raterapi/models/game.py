from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    designer = models.CharField(max_length=50)
    years_released = models.IntegerField()
    num_of_players = models.IntegerField()
    time_to_play = models.IntegerField()
    age = models.IntegerField()