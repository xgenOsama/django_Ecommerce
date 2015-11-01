import json
import datetime

from django.conf import settings
from django.shortcuts import render, HttpResponse, Http404
from django.utils import timezone


# Create your views here.

def dismiss_marketing_message(request):
    if request.is_ajax():
        data = {'success': True}
        json_data = json.dumps(data)
        request.session['dismiss_message_for'] = str(
            timezone.now() + datetime.timedelta(seconds=settings.MARKETING_SECONDS_OFFSET))
        return HttpResponse(json_data, content_type='application/json')
    else:
        raise Http404
