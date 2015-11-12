from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^login/', 'account.views.loginsession'),
    url(r'^logout/', 'account.views.logoutsession'),
    url(r'^renew/', 'account.views.renewssession'),
    url(r'^crsf_cookie/', 'account.views.crsf_cookie')
]