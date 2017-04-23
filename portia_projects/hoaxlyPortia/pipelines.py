from scrapy.exceptions import DropItem

class TypePipeline(object):
    def process_item(self, item, spider):
        if item['_type']:
            item['type'] = item.pop('_type')
            return item
        else:
            raise DropItem("couldnt rename type column for %s" % item)