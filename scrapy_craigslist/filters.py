__author__ = 'htm'

from scrapy.dupefilter import RFPDupeFilter

class NoDuplicateUrl(RFPDupeFilter):
    """A dupe filter that considers the URL"""

    def __init__(self, path=None):
        self.urls_seen = set()
        RFPDupeFilter.__init__(self, path)

    def request_seen(self, request):
        if request.url in self.urls_seen:
            return True
        else:
            self.urls_seen.add(request.url)