from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'taobaoauth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('taobao.urls'), name='taobao'),
    url(r'^identity/', include('identity.urls'), name='identity'),
    url(r'^jd/', include('jd.urls'), name='jd'),
    url(r'^admin/', include(admin.site.urls)),
)
