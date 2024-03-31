from django.core.validators import MaxLengthValidator, MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models


class RunningLineRequest(models.Model):
    text = models.CharField(max_length=128, validators=[MaxLengthValidator(128)])
    duration = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=3)
    width = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(1920)], default=100)
    height = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(1920)], default=100)
    fontsize = models.IntegerField(validators=[MinValueValidator(6), MaxValueValidator(100)], default=30)
    fps = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(144)], default=30)
    date = models.DateTimeField()
