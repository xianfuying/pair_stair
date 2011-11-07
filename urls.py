from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from pairstair.views import add_programmers
from pairstair.views import stairs
from pairstair.views import add


urlpatterns = patterns('',
    url(r'^create/', add_programmers),
    url(r'^stairs/$', stairs),
    url(r'^stairs/(?P<firstMember_id>.+?)/(?P<secondMember_id>.+?)$', add)
    # Examples:
    # url(r'^$', 'learning.views.home', name='home'),
    # url(r'^learning/', include('learning.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
