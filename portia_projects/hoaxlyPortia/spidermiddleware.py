"""
Spider middleware for enriching item with scraped metadata

"""
from __future__ import absolute_import
import pkgutil, inspect

from extruct.w3cmicrodata import MicrodataExtractor

class MicrodataExtruction(object):
    @classmethod

    def process_item(self, item, response):
        mde = MicrodataExtractor()
        data = mde.extract(html)
        debug()
        print(data)
        item['metadata'] = data
        return item