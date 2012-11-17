import hashlib
from django import template
register = template.Library()

@register.simple_tag
def gravatar(author):
    md5 = hashlib.md5(author.email).hexdigest()

    return 'http://www.gravatar.com/avatar/%s?s=180' % md5
