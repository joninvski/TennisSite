from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^tennis/', include('tennis.apps.foo.urls.foo')),
    (r'^people/', 'tennis.people.views.student_list'),


    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),

    #static
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/tennis/media'}),

)
