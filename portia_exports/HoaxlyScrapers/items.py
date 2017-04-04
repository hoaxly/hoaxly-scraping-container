from __future__ import absolute_import

import scrapy
from collections import defaultdict
from scrapy.loader.processors import Join, MapCompose, Identity
from w3lib.html import remove_tags
from .utils.processors import Text, Number, Price, Date, Url, Image


class PortiaItem(scrapy.Item):
    fields = defaultdict(
        lambda: scrapy.Field(
            input_processor=Identity(),
            output_processor=Identity()
        )
    )

    def __setitem__(self, key, value):
        self._values[key] = value

    def __repr__(self):
        data = str(self)
        if not data:
            return '%s' % self.__class__.__name__
        return '%s(%s)' % (self.__class__.__name__, data)

    def __str__(self):
        if not self._values:
            return ''
        string = super(PortiaItem, self).__repr__()
        return string


class FactoidItem(PortiaItem):
    sources = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    editDate = scrapy.Field(
        input_processor=Date(),
        output_processor=Join(),
    )
    category = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    Claim_Header = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    originLinks = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    claimText = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    claim = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    ratingImage = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    researcher = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    Complete = scrapy.Field(
        input_processor=Identity(),
        output_processor=Join(),
    )
    originText = scrapy.Field(
        input_processor=Identity(),
        output_processor=Join(),
    )
    claimMeta = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    complete_content = scrapy.Field(
        input_processor=Identity(),
        output_processor=Join(),
    )
    pubDate = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    ratingMeta = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    claimReviewed = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    originImages = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    subtitle = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
