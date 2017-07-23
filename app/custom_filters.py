#! /usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
from w3lib.url import canonicalize_url


from scrapy.utils.python import to_bytes
from scrapy.dupefilters import RFPDupeFilter


class URLFilter(RFPDupeFilter):
    """A dupe filter that considers the URL"""

    def request_fingerprint(self, request):
        fp = hashlib.sha1()
        fp.update(to_bytes(canonicalize_url(request.url)))

        return fp.hexdigest()
