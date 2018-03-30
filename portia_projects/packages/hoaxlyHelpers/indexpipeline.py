
"""contains custom scrapy pipeline."""

from scrapy.exceptions import DropItem


class IndexPipeline(object):
    """This class renames _index field."""

    def process_item(self, item, spider):
        """implements https://doc.scrapy.org/en/latest/topics/item-pipeline.html#process_item"""
        if item.get('_index'):
            item['self'] = item.pop('_index')
        return item
