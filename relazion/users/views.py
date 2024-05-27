from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpRequest
from users.models import *
from users.forms import *
# Create your views here.
def index(request):
    users_db=Users.objects.all()
    # print(users_db)
    data={
        'users': users_db,
        'me': request.session.get('id')
    }
    return render(request, 'users/index.html', data)
def profil(request):
    # return HttpResponse(request.session["id"])
    if request.session.get('id',None)!="":
        users_db=Users.objects.all()
        sug=Users.objects.order_by('?')[:3]
        users_db=users_db.filter(id=request.session.get('id')).last()
        
        data={
            'user':users_db,
            'users':sug
        }
        return render(request, 'users/profil.html', data)
    else:
        return redirect('login')
def user(request):
    # if request.session['id']!="":
    users_db=Users.objects.all()
    users_db=users_db.filter(id=request.GET["id"]).last()
    if users_db:
        data={
            'user':users_db,
            'me':request.session.get('id'),
            'messages':Messages.objects.filter(id_sender=request.session.get('id'),id_receiver=users_db.id).values().order_by("-id") | Messages.objects.filter(id_sender=users_db.id,id_receiver=request.session.get('id')).values().order_by("-id")
        }
        return render(request, 'users/user.html', data)
    else:
        return redirect('users')
def new_message(request):
    # return HttpResponse(request.POST)
    if (request.method=="POST"):
        # request.POST["id_sender"]=request.session.get('id')    
        form=MessageForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            u=Users.objects.last()
            return redirect('../user/?id='+request.POST["id_receiver"])
        else:
            return HttpResponse("Form no valid")
    else:
        return HttpResponse(request)

def user_search(request):
    if (request.method=="GET"):
        users_db=Users.objects.filter(names__contains=request.GET["search"]).values()
        # print(users_db)
        data={
            'users': users_db,
            'me': request.session.get('id'),
            'search':request.GET["search"]
        }
        return render(request, 'users/index.html', data)
def deconnexion(request):
    request.session["id"]=""
    return redirect('login')