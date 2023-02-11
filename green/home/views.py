from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        name=request.POST.get('name')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')

    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('afilter')

    return render(request,'login.html')

def user(request):
    return render(request,'user.html')

def afilter(request):
    return render(request,'afilter.html')
