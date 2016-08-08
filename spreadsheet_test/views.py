from django.shortcuts import render
from django.http import HttpResponse

from spreadsheet_test import update

def form(request):
  return render(request, 'form.html')

def send(request):
  print('Receive new data：' + request.POST['name'] + '/'
                   + request.POST['birth'] + '/'
                   + request.POST['school'] + '/'
                   + request.POST['dept'])
  myList = [request.POST['name'], request.POST['birth'], request.POST['school'], request.POST['dept']]
  ret = update.update_sheet(myList)
  if ret:
    return HttpResponse('Your information has been submitted !')
  else:
    return HttpResponse('Failed, please contact staff')
