from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.db.models import Q
from django.http import Http404
from django.contrib import messages
from .forms import UserForm
from django.db.models import Case, When

errorm=""

def signUp(request):
    global errorm
    form = UserForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        username=form.cleaned_data['username']	
        password=form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return(redirect("../../home"))
    context={'form':form,'error_message':errorm}
    return render(request,'login.html',context)
    
def Login(request):
    global errorm
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                if user.is_staff:
                    login(request,user)
                    return redirect('index')
                else:
                    login(request,user)
                    return redirect('../../home')
            else:
                return redirect("../signup")
        else:
            errorm="* Invalid Login"
            return redirect("../signup")
    return render(request,'login.html')

def Logout(request):
    logout(request)
    return redirect('../../home')


def index(request):
    return render(request,'index.html')
