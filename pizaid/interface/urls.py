from django.conf.urls import patterns, include, url

urlpatterns = patterns('interface',
    # Examples:
    # url(r'^$', 'pizaid.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'views.index'),
    url(r'^settings/$', 'views.settings'),
)
