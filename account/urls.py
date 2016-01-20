from django.conf.urls import include, url
from django.contrib import admin
import account.views as accountviews

urlpatterns = [
    url(r'^login/', 'account.views.loginsession'),
    url(r'^logout/', 'account.views.logoutsession'),
    url(r'^crsf_cookie/', 'account.views.crsf_cookie'),
    url(r'^loginview/', accountviews.LoginViewAccount.as_view())
]