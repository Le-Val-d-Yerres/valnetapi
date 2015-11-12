from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.core.context_processors import csrf



def loginsession(request):
    username = request.POST['useremail']
    password = request.POST['userpassword']
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


@ensure_csrf_cookie
def crsf_cookie(request):
    csrftoken = csrf(request)['csrf_token']
    print(csrftoken)
    return JsonResponse({'csrf_token': csrftoken})
