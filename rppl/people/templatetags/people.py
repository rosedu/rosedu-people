import hashlib
from django import template
register = template.Library()

from linkicon import LinkIcon

@register.simple_tag
def gravatar(author):
    md5 = hashlib.md5(author.email).hexdigest()

    return 'http://www.gravatar.com/avatar/%s?s=180' % md5

@register.simple_tag
def icon(url):
    return '<a href="%s" class="icon icon-%s"><!-- --></a>' % (url, LinkIcon.icon(url))

