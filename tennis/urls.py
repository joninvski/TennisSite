from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^tennis/', include('tennis.apps.foo.urls.foo')),
    (r'^$', 'tennis.webpage.views.get_home'),
    (r'^services/$', 'tennis.webpage.views.get_services'),
    (r'^contacts/$', 'tennis.webpage.views.get_contacts'),
    (r'^people/', 'tennis.people.views.get_school_student_list'),
    (r'^competition/$', 'tennis.competition.views.get_all_competitions'),
    (r'^competition/(?P<competition_id>\d+)/$', 'tennis.competition.views.get_competition'),
    (r'^competition/(?P<competition_id>\d+)/match/(?P<match_id>\d+)/$', 'tennis.sport.views.get_match_details'),


    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),

    #static
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/tennis/media'}),
)
