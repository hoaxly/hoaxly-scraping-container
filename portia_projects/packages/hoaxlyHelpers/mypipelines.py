
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
