from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.conf.urls import include, url
from django.contrib import admin
from recruitsite.views import welcome, index, register, logout, perror, use_session, complete#, login, logout
from django.contrib.auth.views import login#, logout
from django.contrib.auth.decorators import login_required
from profiles.views import list_student, profile, edit, student_create, other_profile, chatroom, upload, upload_head

admin.autodiscover()
urlpatterns = [
    url(r'^$', index),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login),
    url(r'^index/$', index),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/register/$', register),
  	url(r'^u/$', use_session),

    url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root':'static/img'}),

    url(r'^student_list/$', list_student),
    url(r'^my_profile/$', login_required(profile)),
    url(r'^other_profile/(\d{1,5})/$', login_required(other_profile)),
    url(r'^edit_profile/$', login_required(edit)),
    url(r'^permission_error/$', perror),
    url(r'^create_student/$', login_required(student_create)),
    url(r'^complete/$', complete),
    url(r'^chatroom/(\d{1,5})/(\d{1,5})/$', chatroom),
    url(r'^upload/$', upload),
    url(r'^upload_head/$', upload_head),

]
