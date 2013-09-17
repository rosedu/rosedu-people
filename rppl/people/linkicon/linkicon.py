import re

class LinkIcon:
    links = {
                ".*facebook\.com/.*": "facebook",
                ".*plus\.google\.com/.*": "googleplus",
                ".*twitter\.com/.*": "twitter",
                ".*github\.com/.*": "github",
                ".*linkedin\.com/.*": "linkedin"
            }

    @classmethod
    def icon(cls, url):
        for key, val in cls.links.iteritems():
            if re.match(key, url):
                return val
        return "not_supported"

