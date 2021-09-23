from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class resultmodel(models.Model):
    prn = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length = 100)
    maths = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    science = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    english = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    socialsci = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    hindi = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    
    

    