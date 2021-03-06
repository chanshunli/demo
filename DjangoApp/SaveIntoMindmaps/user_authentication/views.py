from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm

#For user Authentication
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import  csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('SaveEntry'))


def register(request):

    #Assume the newly uploaded registration hasn't been registered before
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password) #Hashing the Password
            user.save()

            profile = profile_form.save(commit=False)
            #Not commit to the databse yet
            #because of collision error
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'user_authentication/registration.html',
                    {'user_form':user_form,
                    'profile_form': profile_form,
                    'registered':registered}
                    )
@csrf_exempt
def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username') #In html file, it finds input with name 'username'
        password = request.POST.get('password')
        #Authentication will be achieved by Django built-in function
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('SaveEntry'))

            else:
                return HttpResponse('Account is not active')
        else:
            print('Someone tried to login and failed!')
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")

    else:
        return render(request, 'user_authentication/login.html',{})
