from django.shortcuts import render

# Create your views here.

import textwrap 
from django.http import HttpResponse
from django.views.generic.base import View

class SignUpView(View):
  def dispatch(request, *args, **kwargs):
    response_text = textwrap.dedent('''\
        <html>
        <head>
        <title> Grand Challenge Django Server Test </title>
        </head>
        <body>
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLScC5mUxI_Ibr__OHLVuGda5Ch5J2pDe89PQerfh2bw0xs_K5g/viewform?embedded=true" width="760" height="500" frameborder="0" marginheight="0" marginwidth="0">載入中…</iframe>
        </body>
        </html>
        ''')
    return HttpResponse(response_text)


#def index(request):
#	return HttpResponse("Hello, world. inside index.")

