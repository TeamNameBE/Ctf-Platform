from django.utils import timezone
from django import template

register = template.Library()


@register.simple_tag
def timeUntil(endTime):
    timeLeft = endTime - timezone.now()

    hours, reste = divmod(timeLeft.seconds, 3600)
    mins, secs = divmod(reste, 60)
    return f"{timeLeft.days} jour(s) {str(hours).zfill(2)}:{str(mins).zfill(2)}"
