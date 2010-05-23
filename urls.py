from django.conf.urls.defaults import *



from django.contrib import admin
admin.autodiscover()
from mlablog.blog.views import *

urlpatterns = patterns('',
    # Example:
    # (r'^mlablog/', include('mlablog.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', home),
)
