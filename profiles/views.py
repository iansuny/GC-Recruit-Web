# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from profiles.models import Student, Interest
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def list_student(request):
#	student1 = { 'name':'陳紹恩', 'department':'IM', 'interest':'', 'talent':'', 'badge':'haha', 'follow':'', 'team':'', 'motto':'hahaha'}
	students = Student.objects.all()
	interests = Interest.objects.all()
	return render_to_response('student_list.html', locals())

def profile(request):
	student = Student.objects.get(name=request.user)
	#students = Student.objects.all()
	return render_to_response('my_profile.html', RequestContext(request, locals()))

@permission_required('profiles.can_edit_base_profile', login_url='/permission_error/')
def edit(request):
	student = Student.objects.get(name=request.user)
	if request.POST:
		motto = request.POST['motto']
		student.motto = motto
		student.save()
		return render_to_response('my_profile.html', RequestContext(request, locals()))
	else:
		return render_to_response('edit_profile.html', RequestContext(request, locals()))
