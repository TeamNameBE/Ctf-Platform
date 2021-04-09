from ctf.models import CTF
from django import template

register = template.Library()


@register.simple_tag
def current_ctf():
    for ctf in CTF.objects.all():
        if ctf.is_now:
            return ctf
