from django.utils import timezone
import pytz

# Converting a datetime to UTC


def make_utc(dt):
    if dt.is_naive():
        dt = timezone.make_aware(dt)
    return dt.astimezone(pytz.utc)
