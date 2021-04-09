import hashlib
from django import template

register = template.Library()


@register.simple_tag
def gravatar(user):
    mail = "".encode("utf8")
    if user.is_authenticated:
        mail = user.email.lower().encode("utf8")
    gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(mail).hexdigest() + "?d=wavatar"

    return gravatar_url
