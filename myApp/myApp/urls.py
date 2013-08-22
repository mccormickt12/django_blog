from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^(?P<uID>\d+)/$', 'blog.views.post', name='Post Id'),
 	url(r'^(?P<uID>\d+)/delete/$', 'blog.views.delete', name='del'),
    url(r'^new/$', 'blog.views.new'),
    url(r'^created/$', 'blog.views.added'),
    # url(r'^myApp/', include('myApp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    
    url(r'^admin/', include(admin.site.urls)),
)
