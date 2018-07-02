from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem, HoaxlyinboxschemaItem


class Politifact(BasePortiaSpider):
    name = "www.politifact.com"
    allowed_domains = ['www.politifact.com']
    start_urls = ['http://www.politifact.com/']
    rules = [
        Rule(
            LinkExtractor(
                allow=('^https\\:\\/\\/politifact\\.com\\/'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[Item(HoaxlyinboxschemaItem,
                   None,
                   '.content',
                   [Field('factoidClaim',
                          '.statement__body *::text',
                          []),
                       Field('factoidRating',
                             '.statement-detail::attr(src)',
                             []),
                       Field('factoidHeadline',
                             '.article__title *::text',
                             []),
                       Field('claimReviewers',
                             '.link::attr(href)',
                             []),
                       Field('factoidPubdate',
                             'span.article__meta *::text',
                             []),
                       Field('itemReviewed',
                             '.article__text > p:nth-child(4) > a::attr(href)',
                             []),
                       Field('factoidSourceUrls',
                             'p:nth-child(10) > .btn::attr(href)',
                             [])])]]
