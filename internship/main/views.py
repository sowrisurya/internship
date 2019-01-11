from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import registerform, loginform
from .models import userspec 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def register(request):
    if request.method == "POST":
        details = request.POST
        print(details)
        flagem = 0
        flagun = 0
        a = User.objects.filter(email = details['email'])
        if a:
            flagem = 1
        b = User.objects.filter(username = details['username'])
        if b:
            flagun = 1

        if details:
            unm =  details['username']		
            context = {
                    'form' : registerform,
                    'uname' : unm,
                    'catg' : 'type',
                }

            context['nbar'] = "register"

            if flagem==0:
                if flagun == 0:
                    print('working')
                    usr = User.objects.create_user(username = unm, email = details['email'], password = details['password'], first_name=details['fname'], last_name=details['lname'])
                    userspec.objects.create(user=usr,username = unm, email = details['email'], first_name=details['fname'], last_name=details['lname'], user_type=details['user_type'])
                    return HttpResponseRedirect('/main/user_login/')

                else:
                    context['eunm'] = 'uname' 
            else:
                context['eem'] = 'email' 
            template = loader.get_template('register.html')
        return HttpResponse(template.render(context,request)) 

    else:
        form = registerform
        context = {'form' : form , 'eem': 0 , 'eunm': 0}
        template = loader.get_template('register.html')
        return HttpResponse(template.render(context,request))

def userlogin(request):
    context = {'form' : loginform}
    if request.method == "POST":
        details = request.POST
        uname = details['username']
        password = details['password']
        try:
            if userspec.objects.get(username=uname).user_type == "user":
                user = authenticate(request, username=uname, password=password)
            
                if user is not None:
                    login(request, user)
                    return HttpResponse("logged in successfully")
                else:
                    context['error'] = "Invalid credentials"
            else:
                context['error'] = "No such user exists. Please register as user"
        except:
            context['error'] = "Please register."

    template = loader.get_template('login.html')
    return HttpResponse(template.render(context,request))

def hospitallogin(request):
    context = {'form' : loginform}
    if request.method == "POST":
        details = request.POST
        uname = details['username']
        password = details['password']
        try:
            if userspec.objects.get(username=uname).user_type == "hospital":
                user = authenticate(request, username=uname, password=password)
            
                if user is not None:
                    login(request, user)
                    return HttpResponse("logged in successfully")
                else:
                    context['error'] = "Invalid credentials"
            else:
                context['error'] = "No such hospital exists. Please register as hospital"
        except:
            context['error'] = "Please register."

    template = loader.get_template('login.html')
    return HttpResponse(template.render(context,request))

def cliniclogin(request):
    context = {'form' : loginform}
    if request.method == "POST":
        details = request.POST
        uname = details['username']
        password = details['password']
        try:
            if userspec.objects.get(username=uname).user_type == "clinic":
                user = authenticate(request, username=uname, password=password)
            
                if user is not None:
                    login(request, user)
                    return HttpResponse("logged in successfully")
                else:
                    context['error'] = "Invalid credentials"
            else:
                context['error'] = "No such clinic exists. Please register as clinic"
        except:
            context['error'] = "Please register."

    template = loader.get_template('login.html')
    return HttpResponse(template.render(context,request))

def sellerlogin(request):
    context = {'form' : loginform}
    if request.method == "POST":
        details = request.POST
        uname = details['username']
        password = details['password']
        try:
            if userspec.objects.get(username=uname).user_type == "seller":
                user = authenticate(request, username=uname, password=password)
            
                if user is not None:
                    login(request, user)
                    return HttpResponse("logged in successfully")
                else:
                    context['error'] = "Invalid credentials"
            else:
                context['error'] = "No such seller exists. Please register as seller"
        except:
            context['error'] = "Please register."

    template = loader.get_template('login.html')
    return HttpResponse(template.render(context,request))

def bloodbanklogin(request):
    context = {'form' : loginform}
    if request.method == "POST":
        details = request.POST
        uname = details['username']
        password = details['password']
        try:
            if userspec.objects.get(username=uname).user_type == "bloodbank":
                user = authenticate(request, username=uname, password=password)
            
                if user is not None:
                    login(request, user)
                    return HttpResponse("logged in successfully")
                else:
                    context['error'] = "Invalid credentials"
            else:
                context['error'] = "No such bloodbank exists. Please register as bloodbank"
        except:
            context['error'] = "Please register."

    template = loader.get_template('login.html')
    return HttpResponse(template.render(context,request))

def diagnosticlogin(request):
    context = {'form' : loginform}
    if request.method == "POST":
        details = request.POST
        uname = details['username']
        password = details['password']
        try:
            if userspec.objects.get(username=uname).user_type == "diagnostic":
                user = authenticate(request, username=uname, password=password)
            
                if user is not None:
                    login(request, user)
                    return HttpResponse("logged in successfully")
                else:
                    context['error'] = "Invalid credentials"
            else:
                context['error'] = "No such diagnostic exists. Please register as diagnostic"
        except:
            context['error'] = "Please register."

    template = loader.get_template('login.html')
    return HttpResponse(template.render(context,request))

