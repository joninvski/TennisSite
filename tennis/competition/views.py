# Create your views here.

from tennis.competition.models import *
from django.shortcuts import *

def get_competition(request, tournament_id):
    """
    Gets the details for a particular competition
    """
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    return render_to_response('competition/competition.html', {
        'tournament': tournament,
        })

def get_all_competitions(none):
    """Gets all competitions"""

    all = Tournament.objects.all()
    return render_to_response('competition/competitions_list.html',{'all_competitions':all,
        })
