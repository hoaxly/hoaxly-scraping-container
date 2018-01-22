"""
Spider middleware for enriching item with scraped metadata
"""

from __future__ import absolute_import

from extruct.w3cmicrodata import MicrodataExtractor
from scrapy.http import Request


class MicrodataExtruction(object):
    """This class extracts microdata."""

    def process_spider_output(self, response, result, spider):
        """get all metadata and add them as fields to item"""
        for x in result:
            if not isinstance(x, Request):
                # only handle items
                mde = MicrodataExtractor()
                data = mde.extract(response.body)
                if data:
                    x['microdata'] = True
                    for field in data:
                        if 'type' in field:
                            x['type'] = field['type']
                        if 'properties' in field:
                            for key, value in field['properties'].items():
                                x[key] = value
                    # yield the enriched item
                    yield x
                else:
                    # if no data set flag and yield the item
                    x['microdata'] = False
                    yield x
            else:
                # yield the request
                yield x
