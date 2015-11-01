import datetime

from django.utils import timezone
from .models import MarketingMessage


def is_offset_is_greater(time_string_offset):
    time_now = str(timezone.now())[:19]
    offset_time = time_string_offset[:19]
    offset_time_formated = datetime.datetime.strptime(offset_time, "%Y-%m-%d %H:%M:%S")
    offset_time_tz_aware = timezone.make_aware(offset_time_formated, timezone.get_default_timezone())
    now_time_formated = datetime.datetime.strptime(time_now, "%Y-%m-%d %H:%M:%S")
    now_time_tz_aware = timezone.make_aware(now_time_formated, timezone.get_default_timezone())
    return now_time_tz_aware > offset_time_tz_aware


class displayMarketing():
    def process_request(self, request):
        try:
            message_offset = request.session['dismiss_message_for']
        except:
            message_offset = None
        try:
            marketing_message = MarketingMessage.objects.get_featured_item().message
        except MarketingMessage.DoesNotExist:
            marketing_message = False

        if message_offset is None:
            request.session['marketing_message'] = marketing_message
        elif message_offset is not None and is_offset_is_greater(message_offset):
            request.session['marketing_message'] = marketing_message
        else:
            try:
                del request.session['marketing_message']
            except:
                pass
