# Create your views here.

from tennis.competition.models import *
from tennis.people.models import *
from django.shortcuts import *

def get_competition(request, competition_id):
    """
    Gets the details for a particular competition
    """
    competition = get_object_or_404(Competition, pk=competition_id)

    competitors_list = Competitor.objects.filter(competition=competition_id)

    return render_to_response('competition/competition.html', {
        'competition': competition,
        'competitors_list': competitors_list,
        })

def get_all_competitions(none):
    """Gets all competitions"""

    all = Competition.objects.all()
    return render_to_response('competition/competitions_list.html',{'all_competitions':all,
        })
