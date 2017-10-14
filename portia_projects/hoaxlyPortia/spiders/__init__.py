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

        for item in result:
            mde = MicrodataExtractor()
            data = mde.extract(response.body)
            if data:
                item['microdata'] = True
                for field in data:
                    if 'type' in field:
                        item['type'] = field['type']
                    if 'properties' in field:
                        for key, value in field['properties'].items():
                            # print value
                            # print key
                            item[key] = value
                # todo: instead of randomly scraping all metadata maybe only
                # scrape the stuff matching our schema?
            print item
            yield item


"""contains custom scrapy pipelines."""

from scrapy.exceptions import DropItem


class TypePipeline(object):
    """This class renames _type field."""

    def process_item(self, item, spider):
        """implements https://doc.scrapy.org/en/latest/topics/item-pipeline.html#process_item"""
        if item['_type']:
            item['schema'] = item.pop('_type')
            return item
        else:
            raise DropItem("couldnt rename type column for %s" % item)
