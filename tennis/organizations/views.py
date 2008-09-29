# Create your views here.

from tennis.organizations.models import *
from django.shortcuts import *

def get_organization(request, organization_id):
    """
    Gets the details for a particular organization
    """
    organization = get_object_or_404(Company , pk=organization_id)
    related_documents = Document.objects.filter(company=organization_id)

    return render_to_response('organizations/organization_detail.html', {
        'organization': organization,
        'related_documents': related_documents,
        })

def get_all_organizations(request):
    """Gets all organizations """

    all = Company.objects.all()

    return render_to_response('organizations/organizations_list.html',
                              {'all_organizations':all,})
