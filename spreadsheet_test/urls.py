from django.conf.urls import url

from spreadsheet_test import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
]
