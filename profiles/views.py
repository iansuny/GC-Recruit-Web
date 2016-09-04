# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from profiles.models import Student, Interest
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def follow_complete(request):
	return render_to_response('follow_complete.html', locals())


def individual_profile(request):
	try:
		student = Student.objects.get(name=request.user)
	except Student.DoesNotExist:
		student=None

	if request.GET.get('id'):
		individual = Student.objects.get(id=request.GET['id'])
		return render_to_response('individual_profile.html', locals())
	elif request.GET.get('follow'):
		individual = Student.objects.get(id=request.GET['follow'])
		student.follow.add(individual)	
		student.save()
		return render_to_response('follow_complete.html', locals())
	else:
		return HttpResponse("errr...")
		

def list_student(request):
#	student1 = { 'name':'陳紹恩', 'department':'IM', 'interest':'', 'talent':'', 'badge':'haha', 'follow':'', 'team':'', 'motto':'hahaha'}
	#if request.user.is_authenticated:
	students = Student.objects.all()
	interests = Interest.objects.all()
	followed = [0]*1000
	try:
		student = Student.objects.get(name=request.user)
		print(student.follow.all())
		for i in students:
			for j in student.follow.all():
				if j==i:
					followed[i.id] = 1
					break
				else:
					followed[i.id] = 0
	except Student.DoesNotExist:
		student=None
	#print(followed)	
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
	if request.POST:
		name = request.user
		realname = request.POST['realname']
		nickname = request.POST['nickname']
		department = request.POST['department']
		motto = request.POST['motto']
		interest = request.POST['interest']
	#	team = request.POST['team']
		talent = request.POST['talent']
#		badge = request.POST['badge']
		#follow = request.POST['follow']
		if any(not request.POST[k] for k in request.POST):
			errors.append('* 有空白欄位！請不要留空！')
		if not errors:
			Student.objects.create(
				realname = realname,
				nickname = nickname,
				department = department,
				motto = motto,
				interest = interest,
				#team = team
				talent = talent,
				#badge = badge
				#follow = follow
			)
		return render_to_response('complete.html', RequestContext(request, locals()))
	else:
		return render_to_response('create_student.html', RequestContext(request, locals()))

