from unicodedata import category
from django.db import models

from raterproject.raterapi.models.categories import Category
from raterproject.raterapi.models.player import Player

class GameCategory:

    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)