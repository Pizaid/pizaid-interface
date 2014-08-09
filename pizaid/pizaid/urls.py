from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import interface
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pizaid.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^interface/', include('interface.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
