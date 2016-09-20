from django.conf.urls import patterns, include, url

urlpatterns = patterns('jd.views',
    url(r'^login/$', 'jd_login', name='jd_login'),
    url(r'^auth/$', 'jd_auth', name='jd_auth'),
    url(r'^query/(?P<nickname>\w+)$', 'jd_query', name='jd_query')
)
