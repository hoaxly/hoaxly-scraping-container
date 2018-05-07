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


class HoaxlyinboxschemaItem(PortiaItem):
    factoidRatingValue = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    factoidClaim = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    claimSource = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    factoidSummary = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    factoidRating = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    factoidReviewers = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    claimReviewers = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    itemReviewed = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    factoidVerdict = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    factoidTags = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    factoidContent = scrapy.Field(
        input_processor=Identity(),
        output_processor=Join(),
    )
    factoidPubdate = scrapy.Field(
        input_processor=Date(),
        output_processor=Join(),
    )
    factoidHeadline = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    claimOrigin = scrapy.Field(
        input_processor=Identity(),
        output_processor=Join(),
    )
    factoidSourceUrls = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
