from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150)