from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app_users.forms import UserForm ,UserProfileInfoForm,CCAProfileInfoform
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView,TemplateView,ListView
from .models import  CCAProfileInfo
from django.urls import reverse_lazy


def index( request):
    return render(request, 'base.html')

def register(request):
    
    registered= False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()
     
            profile = profile_form.save(commit= False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors , profile_forms.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'app_users/registration.html',
                           { 'registered':registered,
                             'user_form':user_form,
                             'profile_form':profile_form})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS DEACTIVATED")
        else:
            return HttpResponse("please use correct id and password")
    else:
        return render(request,'app_users/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'app_users/registration.html',
                            {'registered':registered,
                             'user_form':user_form,
                             'profile_form':profile_form})

def CCA(request):
    registered =False
    if request.method =="POST":
        cca_form =CCAProfileInfoform(data=request.POST)

        if cca_form.is_valid():
            program =cca_form.save(commit=False)
            program.save()
            registered=True
        else:
             print(cca_form.errors)
    else:
        cca_form =CCAProfileInfoform()
    return render(request, 'app_users/CCA.html',
                            {'registered':registered,
                             'cca_form':cca_form})