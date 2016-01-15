from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated


from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.core.context_processors import csrf


from account.models import Message

def loginsession(request):
    username = request.POST['useremail']
    password = request.POST['userpassword']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            message = Message()
            message.status = "ok"
            message.to = "dashboard"
            message.message = "redirection vers le tableau de bord"

            pass
        else:
            # Return a 'disabled account' error message
            pass
    else:
        pass
         # Return an 'invalid login' error message.

    print('pouet')


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        message = Message()
        message.status = "ok"
        message.to = "dashboard"
        message.message = "redirection vers le tableau de bord"
        return Response(message)

    def post(self, request):

        return Response("pouet")

    def get(self, request):
        return Response("pouet")


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
    csrftoken = csrf(request)['csrf_token'] + ""
    return JsonResponse({'csrf_token': csrftoken})



