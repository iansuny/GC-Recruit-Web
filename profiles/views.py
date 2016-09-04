# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from profiles.models import Student, Interest, Chatroom, Team, Badge, Follow, Talent
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone

# Create your views here.
def list_student(request):
#	student1 = { 'name':'陳紹恩', 'department':'IM', 'interest':'', 'talent':'', 'badge':'haha', 'follow':'', 'team':'', 'motto':'hahaha'}
	students = Student.objects.all()
	interests = Interest.objects.all()
	return render_to_response('student_list.html', locals())

@permission_required('profiles.can_view_base_profile', login_url='/create_student/')
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

def student_create(request):
	errors = []
	inter = Interest.objects.all()
	if request.POST:
		name = request.user
		realname = request.POST['realname']
		nickname = request.POST['nickname']
		department = request.POST['department']
		motto = request.POST['motto']
		interest = Interest.objects.get(name='none')
		team = Team.objects.get(name='none')
		talent = Talent.objects.get(name='none')
		badge = Badge.objects.get(name='none')
		follow = Follow.objects.get(name='none')
		# interest = request.POST['interest']
		# team = request.POST['team']
		# talent = request.POST['talent']
		# badge = request.POST['badge']
		# follow = request.POST['follow']
		if any(not request.POST[k] for k in request.POST):
			errors.append('* 有空白欄位！請不要留空！')
		if not errors:
			Student.objects.create(
				name=name,
				realname = realname,
				nickname = nickname,
				department = department,
				motto = motto,
				interest = interest,
				team = team,
				talent = talent,
				badge = badge,
				follow = follow,
			)
		return render_to_response('complete.html', RequestContext(request, locals()))
	else:
		return render_to_response('create_student.html', RequestContext(request, locals()))

def chatroom(request, idfrom, idto):
	s1=Student.objects.get(id=idfrom)
	s2=Student.objects.get(id=idto)
	chatroom1 = Chatroom.objects.filter(student1=s1, student2=s2)
	chatroom2 = Chatroom.objects.filter(student1=s2, student2=s1)
	chatroom = (chatroom1 | chatroom2).order_by('date_time')
	if request.POST:

		content = request.POST['content']
		date_time = timezone.localtime(timezone.now())
		Chatroom.objects.create(
			student1=Student.objects.get(id=idfrom),
			student2=Student.objects.get(id=idto),
			content=content,
			date_time=date_time
		)
	return render_to_response('chatroom.html', RequestContext(request, locals()))

#@permission_required('profiles.can_view_base_profile', login_url='/create_student/')
def other_profile(request,id):
	if id:
		myid = request.user.student_set.first().id
		student = Student.objects.get(id=id)
		return render_to_response('other_profile.html', RequestContext(request, locals()))
	else:
		return HttpResponseRedirect("/student_list/")


