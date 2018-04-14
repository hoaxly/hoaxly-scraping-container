"""
Spider middleware for enriching item with scraped metadata
"""

from __future__ import absolute_import

from scrapy.http import Request

import extruct
import logging


class MicrodataExtruction(object):
    """This class extracts microdata."""

    def process_spider_output(self, response, result, spider):
        """get all metadata and add them as fields to item"""
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        for x in result:
            if isinstance(x, Request):
                # yield the request without making changes
                #logging.debug('this is a request and not an item')
                yield x
            else:
                # if this is an item inspect for microdata
                data = extruct.extract(response.body, response.url)
                if not data:
                    # if no microdata was found set flag and yield the item
                    logging.debug('this item has no microdata')
                    x['hasMetaData'] = False
                else:
                    # if there is microdata parse it to item
                    x['hasMetaData'] = True
                    logging.debug('data is an object of type')
                    logging.debug(type(data))
                    logging.debug('parsing microdata fields')

                    for micodatatype, microdatafields in data.items():
                        logging.debug(micodatatype)
                        logging.debug(microdatafields)
                        x[micodatatype] = microdatafields

                yield x
