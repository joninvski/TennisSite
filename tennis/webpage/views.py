from django.shortcuts import *

# Create your views here.
def get_home(none):
    return render_to_response('static/index.html', {})

def get_services(none):
    return render_to_response('static/services.html', {})

def get_contacts(none):
    return render_to_response('static/contacts.html', {})
