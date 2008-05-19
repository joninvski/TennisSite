from django.shortcuts import *

# Create your views here.
def get_home(request):
    return render_to_response('static/index.html', {})

def get_services(request):
    return render_to_response('static/services.html', {})

def get_contacts(request):
    return render_to_response('static/contacts.html', {})
