from django.contrib import admin

# Register your models here.
# import the models
from .models import *
# register each model with the admin site
admin.site.register(Users)
admin.site.register(Passions)
