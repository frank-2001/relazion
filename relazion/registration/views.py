from django.shortcuts import render
from relazion.relazion.models import Users

def index(request):
    users_db=Users.objects.all()
    data={
        'users':users_db
    }
    return render(request, 'registration/index.html', data)