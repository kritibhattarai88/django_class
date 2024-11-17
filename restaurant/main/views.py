import re
from django.shortcuts import render,redirect
from .models import *
from datetime import datetime
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.

def index(request):
    buff=Momo.objects.filter(category='buff')
    chicken=Momo.objects.filter(category='chicken')
    veg=Momo.objects.filter(category='veg')

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['message']
        Form.objects.create(name=name, email= email, phone=phone, message=msg)

        subject='django training'
        message=render_to_string('main/msg.html',{'name':name,'date':datetime.now()})
        # message = 'Thanks for the form submission'
        from_email='bhattaraikriti.77@gmail.com'
        recipient_list=[email, 'kritibhattarai88@gmail.com']
        send_mail(subject,message,from_email,recipient_list,fail_silently=True)
        
    return render(request,'main/index.html',{'buff':buff,'chicken':chicken,'veg':veg})


def about(request):
    return render(request,'main/about.html')


def contact(request):
    return render(request,'main/contact.html')

@login_required(login_url='log_in')
def menu(request):
    return render(request,'main/menu.html')


def services(request):
    return render(request,'main/services.html')

def terms(request):
    return render(request, 'main/terms.html')

def privacy(request):
    return render(request, 'main/privacy.html')

def policy(request):
    return render(request, 'main/policy.html')

def support(request):
    return render(request, 'main/support.html')



#--------------------- AUTHENTICATION-------------------#

def log_in(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        if not User.objects.filter(username=username).exists():
            messages.error('Username is not registered!')
            return redirect('log_in')
        user=authenticate(username=username, password=password)#user is a variable

        if user is not None:
            login(request,user)
            if remember_me:#true
                request.session.set_expiry(1200000)
            else:
                request.session.set_expiry(0)

            messages.success(request, "Login successfully!!")
            return redirect('index')
        else:
            messages.error(request, "Invalid password!")
            return redirect('log_in')


    return render(request,'auth/login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']

        if password==password1:
            try:
                 validate_password(password)
                 if User.objects.filter(username=username).exists():
                    messages.error(request, "Username already exists")
                    return redirect('register')
                 elif User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return redirect('register')
                 elif username.lower() in password.lower():
                     messages.error(request,"Password cannot be too similar to username.")
                     return redirect('register')
                 elif not re.search(r'[A-Z]',password):
                    messages.error(request,"Password must contain atleast one uppercase letter.")
                    return redirect('register')
                 elif not re.search(r'\d', password):
                     messages.error(request, "Password must contain atleast one digit.")
                     return redirect('register')
                 elif not re.search(r'[@#%$<>]', password):
                     messages.error(request, "Password must contain atleast one special character.")
                     return redirect('register')
                 
                 else:
                   User.objects.create_user(first_name=first_name, last_name=last_name,email=email,username=username,password=password)
                   messages.success(request, "Registered successfully!")
                   return redirect('log_in')
                 
            except ValidationError as e:
                for error in e.messages:
                    messages.error(request,error)
                return redirect('register')

           
        else:
            messages.error(request,"Your passwords doesn't match")
            return redirect('register')

    return render(request,'auth/register.html')

def log_out(request):
    logout(request)
    return redirect('log_in')

# @login_required(login_url='log_in')
def change_password(request):
    form = PasswordChangeForm(user=request.user)
    if request.method=='POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')


        
    return render(request, 'auth/change_password.html', {'form':form})