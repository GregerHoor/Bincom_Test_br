from django.http import JsonResponse
from django.utils import timezone

from .models import *

import json




def get_user_ip(request):
    x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
    if isinstance(x_forwarded, list):
        ip = x_forwarded[0]
    elif isinstance(x_forwarded, str):
        ip = x_forwarded.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def create_polling_data(request):
    data = json.loads(request.body)
    payload = data.get('payload')
    
    lga_id = payload.get('lga')
    party_id = payload.get('party')
    ward_id = payload.get('ward')
    unit = payload.get('unit')
    polling_unit_num = payload.get('polling_unit_num')
    polling_unit_name = payload.get('polling_unit_name')
    polling_unit_desc = payload.get('polling_unit_desc')
    entered_by_user = payload.get('entered_by_user')
    lat = payload.get('lat')
    long = payload.get('long')
    user_ip_address = get_user_ip(request)
    
    agent = Agentname.objects.filter(name_id=entered_by_user).first()
    lga = Lga.objects.filter(uniqueid=lga_id).first()
    ward = Ward.objects.filter(uniqueid=ward_id).first()
    
    PollingUnit.objects.create(polling_unit_id=unit, ward_id=ward.ward_id, lga_id=lga.lga_id, uniquewardid=ward.uniqueid , polling_unit_number=polling_unit_num, polling_unit_name=polling_unit_name, polling_unit_description=polling_unit_desc, entered_by_user=agent.firstname,lat=lat, long=long, date_entered=timezone.now(), user_ip_address=user_ip_address)
    
    response = {
        'success':True,
        'message':"You successfully addeed a new polling unit.",
    }
    return JsonResponse(response)