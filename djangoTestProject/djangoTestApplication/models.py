from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    sinopsis = models.TextField(max_length=1024)
    # portrait

class MovieCritic(models.Model):
    title =  models.CharField(max_length=50)
    critic = models.TextField(max_length=1000000)
    score = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    created_by =  models.CharField(max_length=50, default="")
    # is_public que diga si se ve en la grid publica o no
    