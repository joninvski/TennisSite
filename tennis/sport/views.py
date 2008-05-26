# Create your views here.
from tennis.sport.models import *
from django.shortcuts import *

def get_match_details(request, competition_id, match_id):
    """
    
    
    request -- 
    competitor -- 
    """
    match = get_object_or_404(SingleMatch, pk=match_id)
    competitorAresult = match.get_results_by_competitor(match.competitorA)
    competitorBresult = match.get_results_by_competitor(match.competitorB)

    return render_to_response('sport/match_detail.html', {'match':match,
                                                         'competitorAresult':competitorAresult,
                                                          'competitorBresult':competitorBresult,
                                                         })
