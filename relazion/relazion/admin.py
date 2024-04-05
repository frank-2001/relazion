from django.contrib import admin
# import the models
from .models import *
# register each model with the admin site
admin.site.register(Users)
admin.site.register(Messages)
admin.site.register(Passions)