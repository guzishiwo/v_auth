#!/usr/bin/env python
#coding=utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('identity.views',
    url(r'login$', 'auth_login', name='identity_login'),
    url(r'logout$', 'auth_logout', name='identity_logout'),
)

