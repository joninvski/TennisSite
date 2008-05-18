from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^tennis/', include('tennis.apps.foo.urls.foo')),
    (r'^$', 'tennis.webpage.views.get_home'),
    (r'^services/$', 'tennis.webpage.views.get_services'),
    (r'^contacts/$', 'tennis.webpage.views.get_contacts'),
    (r'^people/', 'tennis.people.views.student_list'),
    (r'^competition/$', 'tennis.competition.views.get_all_competitions'),
    (r'^competition/(?P<competition_id>\d+)/$', 'tennis.competition.views.get_competition'),


    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),

    #static
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/tennis/media'}),
)
