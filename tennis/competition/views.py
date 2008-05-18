# Create your views here.

from tennis.competition.models import *
from django.shortcuts import *

def get_competition(tournament_id):
    """
    Gets the details for a particular competition
    """
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    return render_to_response('competition/competition.html', {
        'tournament': tournament,
        })
