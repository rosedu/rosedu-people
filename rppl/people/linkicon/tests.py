from django.test import TestCase
from linkicon import LinkIcon

class LinkIconTest(TestCase):
    def test_facebook(self):
        self.assertEqual(LinkIcon.icon("https://www.facebook.com/mm.bivol"), "facebook")

    def test_googleplus(self):
        self.assertEqual(LinkIcon.icon("https://plus.google.com/102414295336553974068/posts"), "googleplus")

    def test_none(self):
        self.assertEqual(LinkIcon.icon("loremipsum"), "not_supported")

