"""
Spider middleware for enriching item with scraped metadata

"""
from __future__ import absolute_import
import pkgutil, inspect

from extruct.w3cmicrodata import MicrodataExtractor
from scrapy.http import Request
from scrapy import log
import os.path
import pprint

class MicrodataExtruction(object):

    def process_spider_output(self, response, result, spider):
        items = []
        for x in result:
            mde = MicrodataExtractor()
            data = mde.extract(response.body)
            x['metadata'] = data
            yield x
