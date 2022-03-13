from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class Pool(models.Model):

    name = models.TextField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Player(models.Model):
    name = models.TextField(blank=False, null=False)
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE)

class Game(models.Model):
    team_1 = models.TextField(blank=False, null=False)
    team_2 = models.TextField(blank=False, null=False)
    winner = models.TextField(blank=False, null=False)
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE) 

class Pick(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE) 
    player = models.ForeignKey(Player, on_delete=models.CASCADE) 
    choice = models.TextField(blank=False, null=False)
    win= models.BooleanField(null=True)