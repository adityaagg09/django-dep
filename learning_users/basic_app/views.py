from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm

# for login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("You are login cool")

# isne apne app logout krdia isko balle balle ,  @ agr yeh hoga toh chlega iski gaaadi
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index')) # isse apne page index pe ajayaga 







def register(request):
    registered=False
    
    if request.method == 'POST':

        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save() # data jo bhi aya usko save
            user.set_password(user.password) # isse hash wala chlega 
            user.save() # saving the hash password one 

            profile=profile_form.save(commit=False) 
            # isme jo registered user ka bhi data firse save ho jaiga 
            profile.user=user 
            # isse purane wale ko attach krdia

            # agr kuch bhi file input li ha toh hm uske ander yeh likhna padega 
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic'] # jo naam hmne model me dia 
        
            profile.save()

            registered=True
            print("Hello")

        else:
            print(user_form.errors,profile_form.errors)
    
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request,'basic_app/registration.html',
    {
        'user_form': user_form,
        'profile_form' : profile_form,
        'registered' : registered
    })


# yeh name hmne apna .html and settings mein bhi same rkkha ha 
def user_login(request):

    
    if request.method == 'POST':
        # fetching our username and password
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)

        # verfying the username and password
        user=authenticate(username=username,password=password)
        print(user)

        # agr verfied hogya user toh 
        if user:
            # ager account active ha toh 
            if user.is_active:
                login(request,user) #login krdo
                return HttpResponseRedirect(reverse('index'))
            
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someoen  try to login and fail")
            print(username,password)
            return HttpResponse("INvalid login detials")
    else:
        return render(request,'basic_app/login.html',{})









