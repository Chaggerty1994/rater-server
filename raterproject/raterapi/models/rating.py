from tkinter import CASCADE
from django.db import models

from raterproject.raterapi.models.game import Game
from raterproject.raterapi.models.player import Player

class Rating(models.Model):

    rating = models.IntegerField
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE )
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)