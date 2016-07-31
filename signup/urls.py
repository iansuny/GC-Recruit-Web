from django.conf.urls import url

from signup.views import SignUpView

urlpatterns = [
	url(r'^$', SignUpView.as_view(), name='SignUpView'),
]

