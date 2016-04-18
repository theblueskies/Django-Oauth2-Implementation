"""provider URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from authorize import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^list_user/$', views.RestrictedListUserEndpoint.as_view()),
    url(r'^sign_up/$', views.SignUp.as_view()),

    # For the oauth2 supplied URLS eg: o/applications
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # For the login on DRF Browsable API
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
