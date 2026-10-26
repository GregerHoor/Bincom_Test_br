from django.shortcuts import render

# Create your views here.

import os 

import psycopg
from psycopg.types.json import Jsonb

from .models import *

def home_page(request):
    polling_all = PollingUnit.objects.all
    lga_all = Lga.objects.all
    context = {
        'polling_all':polling_all,
        'lga_all':lga_all,
    }
    return render(request, 'Templates/Main/all_polling.html', context)



def polling_unit(request, uniqueid):
    polling_unit = PollingUnit.objects.filter(uniqueid=uniqueid).first()
    lga_unit = Lga.objects.filter(lga_id=polling_unit.lga_id).first()
    ward_unit = Ward.objects.filter(ward_id=polling_unit.ward_id).first()
    
    context = {
        'p_unit':polling_unit,
        'lga_unit':lga_unit,
        'ward_unit':ward_unit,
    }
    return render(request, 'Templates/Main/polling_unit.html', context)



def form_page(request):
    lga_all = Lga.objects.all
    agent_all = Agentname.objects.all
    party_all = Party.objects.all
    ward_all = Ward.objects.all
    context = {
        'lga_all':lga_all,
        'agent_all':agent_all,
        'party_all':party_all,
        'ward_all':ward_all,
    }
    return render(request, 'Templates/Main/form.html', context)
