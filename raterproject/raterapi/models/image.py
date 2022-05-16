from django.contrib.auth.models import User
from django.db import models
from raterproject.raterapi.models.game import Game
from raterproject.raterapi.models.player import Player


class Image(models.Model):

    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=250)