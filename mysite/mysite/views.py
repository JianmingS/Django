#coding=utf-8
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
import datetime
from django.shortcuts import render_to_response
from books.models import Book
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def hello (request):
  return HttpResponse("Hello world!")
'''
def current_datetime(request) :
  now = datetime.datetime.now()
  t = get_template('current_datetime.html')
  html = t.render(Context({'current_date': now}))
  #html = "<html><body>It is now %s.</body></html>" % now
  return HttpResponse(html)
'''

'''
# simplify 1
def current_datetime(request) :
  now = datetime.datetime.now()
  return render_to_response('current_datetime.html', {'current_date': now})
'''
# simplify 2
def current_datetime(request) :
  current_date = datetime.datetime.now()
  return render_to_response('current_datetime.html', locals())
# simplify 3
def current_datetime(request) :
  now = datetime.datetime.now()
  return render_to_response('current_datetime.html', {'current_date': now})

'''
def hours_ahead(request, offset) :
  try:
    offset = int(offset)
  except ValueError:
    raise Http404()
  dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
  #assert False
  html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
  return HttpResponse(html)
'''
# simplify 1
def hours_ahead(request, offset) :
  try:
    offset = int(offset)
  except ValueError:
    raise Http404()
  dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
  return render_to_response('hours_ahead.html', {'hour_offset': offset, 'next_time': dt})

'''
def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
'''
def search_form(request):
    return render_to_response('search_form.html')
''' 
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',
            {'books': books, 'query': q})
    else:
        return render_to_response('search_form.html', {'error': True})
        #return HttpResponse('Please submit a search term.')
'''
def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html',
        {'errors': errors})
     

