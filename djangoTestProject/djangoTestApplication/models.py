from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Movie(models.Model):
    title =  models.CharField(max_length=50)
    critic = models.TextField(max_length=1024)
    score = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
