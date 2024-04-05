from datetime import date
from django.db import models

# Create your models here.
class Messages(models.Model):
    id_sender=models.ForeignKey("users.Users",on_delete=models.CASCADE,null=False,blank=False,related_name="senders")
    id_receiver=models.ForeignKey("users.Users",on_delete=models.CASCADE,null=False,blank=False,related_name="receivers")
    message=models.TextField()
    creation_date=models.DateField(default=date.today)
    def __str__(self):
        return self.message