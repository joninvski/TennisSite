# Create your views here.
from tennis.people.models import *
from django.shortcuts import render_to_response, get_object_or_404

def student_list(request):
    all = Student.objects.all()
    return render_to_response('people/all_students.html',{'all_students':all,
        })
