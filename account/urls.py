from django.conf.urls import include, url
from django.contrib import admin
from account import views
urlpatterns = [
    url(r'^login/', views.loginsession),
    url(r'^logout/', views.logoutsession),
    url(r'^crsf_cookie/', views.crsf_cookie),
    
]