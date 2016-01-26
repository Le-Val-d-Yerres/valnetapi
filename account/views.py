from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
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
            message.msg = "Authentification réussie. Redirection vers le tableau de bord."
            return JsonResponse(message.getdict())
        else:
            message = Message()
            message.status = "error"
            message.to = "login"
            message.msg = "Ce compte est inactif contacter l'administrateur"
            return JsonResponse(message.getdict())
    else:
        message = Message()
        message.status = "error"
        message.to = "login"
        message.msg = "Soit ce compte n'existe pas soit le mot de passe n'est pas le bon."
        return JsonResponse(message.getdict())


def logoutsession(request):
    logout(request)


@ensure_csrf_cookie
def crsf_cookie(request):
    csrftoken = csrf(request)['csrf_token'] + ""
    return JsonResponse({'csrf_token': csrftoken})



