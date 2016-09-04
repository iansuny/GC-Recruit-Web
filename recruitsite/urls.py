from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.conf.urls import include, url
from django.contrib import admin
from recruitsite.views import welcome, index, register, logout, perror, use_session, complete#, login, logout
from django.contrib.auth.views import login#, logout
from django.contrib.auth.decorators import login_required

from profiles.views import list_student, profile, edit, student_create, individual_profile, follow_complete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', login),
    url(r'^index/$', index),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/register/$', register),
  	url(r'^u/$', use_session),

    url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root':'static/img'}),

    url(r'^student_list/$', list_student),
    url(r'^my_profile/$', login_required(profile)),
    url(r'^edit_profile/$', login_required(edit)),
    url(r'^permission_error/$', perror),
    url(r'^create_student/$', login_required(student_create)),
    url(r'^complete/$', complete),

    url(r'^individual_profile/$', individual_profile),
    url(r'^follow_complete/$', follow_complete),

]
