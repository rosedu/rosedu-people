from django.conf.urls.defaults import patterns, url

from views import (Overview, Profile, Projects, ProjectDetail, ProfileSetup,
                   ProfileCreate)

urlpatterns = patterns('',
    url(r'^$', Overview.as_view(), name='overview'),
    url(r'login/$', 'django.contrib.auth.views.login',
        {'template_name': 'people/login.html'}),
    url(r'logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}),
    url(r'password_change/', 'django.contrib.auth.views.password_change',
        {'post_change_redirect': '/',
         'template_name': 'people/change_password.html'}),
    url(r'^profile_create$', ProfileCreate.as_view(), name='profile-create'),
    url(r'^profile/(?P<pk>\d+)/$', Profile.as_view(), name='profile'),
    url(r'^project/$', Projects.as_view(), name='project-list'),
    url(r'^project/(?P<pk>\d+)/$', ProjectDetail.as_view(), name='project-detail'),
    url(r'^profile_set/(?P<pk>\d+)', ProfileSetup.as_view(), name='profile-setup'),
)
