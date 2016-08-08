from django.shortcuts import render
from django.http import HttpResponse

def form(request):
  return render(request, 'form.html')

def send(request):
  print('新資料：' + request.POST['name'] + '/'
                   + request.POST['birth'] + '/'
                   + request.POST['school'] + '/'
                   + request.POST['dept'])
  return HttpResponse('Your information has been submitted !')
