import json
import re

class LinkIcon:
    links = {
                ".*facebook\.com/.*": "facebook",
                ".*plus\.google\.com/.*": "googleplus"
            }

    @classmethod
    def icon(cls, url):
        for key, val in cls.links.iteritems():
            if re.match(key, url):
                return val
        return "not_supported"

