from django.db import models
from django.db.models.deletion import CASCADE


class Game(models.Model):
    title = models.CharField(max_length=75)
    maker = models.CharField(max_length=50)
    skillLevel = models.IntegerField()
    gamer = models.ForeignKey("Gamer", on_delete=CASCADE)
    gameTypeId = models.ForeignKey(
        "GameType", on_delete=CASCADE, related_name="games")
    numberOfPlayers = models.IntegerField()
