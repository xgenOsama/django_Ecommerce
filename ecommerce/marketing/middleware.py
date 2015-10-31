import datetime

from django.utils import timezone
from .models import MarketingMessage


class displayMarketing():
    def process_request(self, request):
        print timezone.now() + datetime.timedelta(hours=8)
        try:
            request.session['marketing_message'] = MarketingMessage.objects.get_featured_item().message
        except MarketingMessage.DoesNotExist:
            request.session['marketing_message'] = False
