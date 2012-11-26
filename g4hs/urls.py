from django.conf.urls import patterns, include, url
from register import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.index, name="home"),
	url(r'submit/$', views.submit, name="submit"),
	url(r'confirm/(.+)/$', views.confirm, name="confirm"),
	url(r'done/$', views.done, name="done"),
    # Examples:
    # url(r'^$', 'g4hs.views.home', name='home'),
    # url(r'^g4hs/', include('g4hs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)
