from django.db import models
from django.core import validators

# Create your models here.


class School(models.Model):
    Sid=models.IntegerField(primary_key=True,validators=[validators.MinValueValidator(100)])
    Sname=models.CharField(max_length=100, validators=[validators.RegexValidator('[A-Z]')])
    Saddress=models.TextField()
    Smail=models.EmailField()


    def __str__(self):
        return self.Sname