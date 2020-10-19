from django.shortcuts import render,redirect
from .models import Destination, Complaints, Guides
from django.core import mail

def home(request):
    dests=Destination.objects.all()
    return render(request,'home.html', {'dests':dests})

def about(request):
    return render(request,'about.html')

def places(request,place):
    if place=='null':
        if request.method == 'POST':
            place = request.POST['location']
        location=place.upper()
        if request.user.is_authenticated:
            if Destination.objects.filter(place=location).exists():
                dest=Destination.objects.filter(place=location).values()
                guide=Guides.objects.filter(place=location).values()
                return render(request, 'place.html', {'place':location,'dest':dest, 'guide':guide})
            else:
                return redirect('/')
        else:
            return redirect('login')
    else:
        if request.user.is_authenticated:
            dest=Destination.objects.filter(place=place).values()
            guide=Guides.objects.filter(place=place).values()
            return render(request,'place.html',{'place':place,'dest':dest, 'guide':guide})
        else:
            return redirect('login')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        body = request.POST.get('body')
        compl = Complaints(name=name, subject=subject, complaint=body)
        compl.save()
        return render(request,'contact.html',{"message":"Message Sent!"})
    else:
        return render(request,'contact.html',{"message":""})

def bookings(request):
    return render(request,'bookings.html')