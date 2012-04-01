from django.conf.urls.defaults import patterns, include, url

from views import Overview, Profile, Activities, ActivityDetail, EditionDetail, VersionDetail

urlpatterns = patterns('',
    url(r'^$', Overview.as_view(), name='overview'),
    url(r'^profile/(?P<pk>\d+)/$', Profile.as_view(), name='profile'),
    url(r'^activity/$', Activities.as_view(), name='activity-list'),
    url(r'^activity/(?P<pk>\d+)/$', ActivityDetail.as_view(), name='activity-detail'),
    url(r'^edition/(?P<pk>\d+)/$', EditionDetail.as_view(), name='edition-detail'),
    url(r'^version/(?P<pk>\d+)/$', VersionDetail.as_view(), name='version-detail'),
)
