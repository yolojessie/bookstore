from django.db import models
import random
# Create your models here.

class Guess(models.Model):
    answer = random.randint(1,9)
    guessNum = -1