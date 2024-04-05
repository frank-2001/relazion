from datetime import date
from django.db import models

class Users(models.model):
    names=models.CharField(null=False,blank=False)
    birth=models.DateField()
    sex=models.CharField()
    color=models.CharField()
    height=models.FloatField()
    photo=models.FileField()
    passions=models.CharField()
    creation_date=models.DateField(default=date.today)

class Messages(models.Model):
    id_sender=models.IntegerField(null=False,blank=False)
    id_receiver=models.IntegerField(null=False,blank=False)
    message=models.TextField()
    creation_date=models.DateField(default=date.today)

class Passions(models.Model):
    name=models.CharField(null=False,blank=False)