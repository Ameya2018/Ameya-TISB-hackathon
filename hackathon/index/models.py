from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
class Info(models.Model):
    GPA = models.PositiveIntegerField("GPA - Enter from 1-5", default='', validators=[MinValueValidator(1), MaxValueValidator(5)])
    SATM = models.PositiveIntegerField("SAT MATHS - Enter from 1-800",default='' , validators=[MinValueValidator(1), MaxValueValidator(800)])
    SATE=models.PositiveIntegerField("SAT ENGLISH - Enter from 1-800" ,default='' , validators=[MinValueValidator(1), MaxValueValidator(800)])
    ACT=models.PositiveIntegerField("ACT SCORE - Enter from 1-36" , blank = False , validators=[MinValueValidator(1), MaxValueValidator(36)])
  