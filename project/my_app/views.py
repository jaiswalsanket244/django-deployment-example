from django.shortcuts import render
from my_app.forms import User_form, User_profile_info_form
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def Home_view(request):
    return render(request,'my_app/Home_page.html')

def registration(request):
    registered = False
    if request.method == 'POST':
        user_form = User_form(data=request.POST)
        user_profile_form = User_profile_info_form(data=request.POST)

        if user_form.is_valid and user_profile_form.is_valid:
            user = user_form.save()
            user.set_password(user.password)
            user.save() 

            profile =  user_profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered =  True
        else:
            print(user_form.errors,user_profile_form.errors)

    else:

        user_form = User_form()
        user_profile_form = User_profile_info_form()

    return render(request,'my_app/registration.html',{'user_form':user_form,'user_profile_form':user_profile_form,'registered':registered})

@login_required
def special_view(request):
    return HttpResponse('YOu are logged in Nice')
  
@login_required
def user_logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('Home_view'))

def user_login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password= request.POST.get("password")

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('Home_view'))

            else:
                return HttpResponse('Account not active')

        else:
            print('Login Failed Invaid Credientirals')
            return HttpResponse('invalid login details ')
    else:
        return render(request,'my_app/Login.html',{})