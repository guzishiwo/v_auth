from django.conf.urls import patterns, include, url

urlpatterns = patterns('taobao.views',
    url(r'^login/$', 'login', name='taobao_login'),
    url(r'^auth/$', 'auth', name='taobao_auth'),
    url(r'^query/(?P<nickname>\w+)$', 'query', name='taobao_query')
)