from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Member
# Create your views here.

def index(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'web/index.html')

def login(request):
    return render(request, 'web/login.html')

def home(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'web/home.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'web/login.html', context)

