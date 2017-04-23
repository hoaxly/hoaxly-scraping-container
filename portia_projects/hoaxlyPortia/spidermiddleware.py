"""
Spider middleware for enriching item with scraped metadata

"""

from __future__ import absolute_import

from extruct.w3cmicrodata import MicrodataExtractor
from scrapy.http import Request


class MicrodataExtruction(object):
    """This class extracts microdata."""

    def process_spider_output(self, response, result, spider):
        """implements https://doc.scrapy.org/en/latest/topics/spider-middleware.html#scrapy.spidermiddlewares.SpiderMiddleware.process_spider_output"""

        for item in result:
            mde = MicrodataExtractor()
            data = mde.extract(response.body)
            item['metadata'] = data
            yield item
