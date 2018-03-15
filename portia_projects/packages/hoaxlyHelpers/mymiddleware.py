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
                # yield the request
                yield x
            else:
                # only handle items
                data = extruct.extract(response.body, response.url)
                if not data:
                    # if no microdata was found set flag and yield the item
                    x['hasMetaData'] = False
                    yield x
                else:
                    # if there is microdata parse it to item
                    x['hasMetaData'] = True
                    logging.debug('data is an object of type')
                    logging.debug(type(data))
                    logging.debug('parsing microdata fields')
                    for field in data:
                        logging.debug('check if there is microdata in field')
                        logging.debug(data.get(field))
                        if data.get(field):
                            logging.debug('there is microdata in field.')
                            logging.info('Appending values to item')
                            logging.debug(data.get(field))
                            x['metadata'] = data.get(field)
                    yield x
