# Create your views here.
from tennis.people.models import *
from django.shortcuts import render_to_response, get_object_or_404

def get_students_list(request):
    all_school = SchoolStudent.objects.all()
    all_club = ClubStudent.objects.all()
    return render_to_response('people/all_students.html',
                              {'all_school_students':all_school,
                               'all_club_students':all_club, })

def get_person(request, person_id):
    """
    Gets the details for a particular competition
    """
    person = get_object_or_404(Person, pk=person_id)


    return render_to_response('people/person_detail.html', {
        'person': person,
        })
