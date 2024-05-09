from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpRequest
from users.models import *

# Create your views here.
def index(request):
    users_db=Users.objects.all()
    # print(users_db)
    data={
        'users':users_db
    }
    return render(request, 'users/index.html', data)
def profil(request):
    # return HttpResponse(request.session["id"])
    if request.session.get('id',None)!="":
        users_db=Users.objects.all()
        users_db=users_db.filter(id=request.session['id']).last()
        data={
            'user':users_db
        }
        return render(request, 'users/profil.html', data)
    else:
        return redirect('login')
def user(request):

    # if request.session['id']!="":
    users_db=Users.objects.all()
    users_db=users_db.filter(id=request.session.get('id')).last()
    if users_db:
        data={
            'user':users_db
        }
        return render(request, 'users/user.html', data)
    else:
        return redirect('users')
def deconnexion(request):
    request.session["id"]=""
    return redirect('login')