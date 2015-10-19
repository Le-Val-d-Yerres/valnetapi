from django.shortcuts import render
from django.contrib.auth import authenticate, login


def loginsession(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            pass
        else:
            # Return a 'disabled account' error message
            pass
    else:
        pass
         # Return an 'invalid login' error message.

    print('pouet')

def logoutsession(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            pass
        else:
            # Return a 'disabled account' error message
            pass
    else:
        pass
         # Return an 'invalid login' error message.


def renewsession(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            pass
        else:
            # Return a 'disabled account' error message
            pass
    else:
        pass
         # Return an 'invalid login' error message.