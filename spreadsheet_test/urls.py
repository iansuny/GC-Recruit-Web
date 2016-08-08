from django.conf.urls import url

from spreadsheet_test import views

urlpatterns = [
  url(r'^$', views.form, name='form'),
  url(r'^send/$', views.send, name='send'),
]
