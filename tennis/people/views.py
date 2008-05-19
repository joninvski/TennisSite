# Create your views here.
from tennis.people.models import *
from django.shortcuts import render_to_response, get_object_or_404

def get_school_student_list(request):
    all = SchoolStudent.objects.all()
    return render_to_response('people/all_school_students.html',{'all_school_students':all,
        })
