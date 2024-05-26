from datetime import date
from django.db import models

# Create your models here.
class Users(models.Model):
    names=models.CharField(null=False,blank=False,max_length=100)
    birth=models.DateField()
    sex=models.CharField(max_length=20)
    color=models.CharField(max_length=20)
    height=models.FloatField()
    photo=models.FileField()
    passions=models.CharField(max_length=50,null=True)
    creation_date=models.DateField(default=date.today)
    password=models.CharField(max_length=100,default='1234')
    

class Messages(models.Model):
    id_sender=models.IntegerField(null=False,blank=False)
    id_receiver=models.IntegerField(null=False,blank=False)
    message=models.TextField()
    creation_date=models.DateField(default=date.today)

class Passions(models.Model):
    name=models.CharField(null=False,blank=False,max_length=100)
    def __str__(self):
        return self.name
    