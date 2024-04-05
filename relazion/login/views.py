from django.http import HttpResponse
from django.shortcuts import redirect, render

from users.forms import LoginForm, UsersForm
from users.models import Users
# from relazion.relazion.models import Users

# Create your views here.
def index(request):
    if request.session['id']=='':
        return render(request,"login/index.html")
    else:
        return redirect('profil')
def login(request):
    if (request.method=="POST"):
        form=LoginForm(request.POST)
        if form.is_valid():
            print(form.data)
            u=Users.objects.filter(id=form.data.get('id'),password=form.data.get('password'))
            if(u):
                # print(u.id)
                request.session['id']=form.data.get('id')
                return redirect('profil')
            else:
                return render(request,"login/index.html",{"message":"Mot de pass ou Id incorect"})
                
        else:
            return render(request,"login/index.html",{"message":"From no valid"})
    else:
        return render(request,"login/index.html",{"message":"Method no valid"})
def registration(request):
    if request.session['id']=='':
        return render(request,"login/registration.html")
    else:
        return redirect('profil')
def new(request):
    if (request.method=="POST"):
        form=UsersForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            u=Users.objects.last()
            return render(request,"login/index.html",{"message":"User saved, your ID is "+str(u.id)})
        else:
            return render(request,"login/registration.html",{"message":"From no valid"})
    else:
        return render(request,"login/registration.html",{"message":"Method no valid"})