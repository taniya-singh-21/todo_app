from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    return(request,'home.html')

def register(request):
    if request.method == 'POST':
        usrname = request.POST.get('username')
        usremail = request.POST.get('email')
        usrpswd = request.POST.get('pass1')
        usrpswd2 = request.POST.get('pass2')
        if usrpswd == usrpswd2:
            if User.objects.filter(username=usrname).exists:
                messages.info(request,'username already taken')
                return redirect('/')
            elif User.objects.filter(email=usremail).exists:
                messages.info(request,'email already taken')
                return redirect('/')
            else:
                user = User.objects.create_user(username=usrname,password=usrpswd,email=usremail)
                user.save()
        else:
                messages.info(request,'password does not match')
                return redirect('/')
        return redirect('login')
        
        
    return render(request,'register.html')
def login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'home.html')
    
        else :
            messages.info(request,"lack Credentials")
            return redirect ('login')
       
    return render(request,'login.html')

def logout(request):   
         auth.logout(request)
      
         return redirect('login')

        