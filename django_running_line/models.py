from django.core.validators import MaxLengthValidator
from django.db import models


class RunningLineRequest(models.Model):
    text = models.CharField(max_length=128, validators=[MaxLengthValidator(128)])
    date = models.DateTimeField()
