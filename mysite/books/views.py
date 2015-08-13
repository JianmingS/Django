from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def search_form(request):
    return render_to_response('search_form.html')
