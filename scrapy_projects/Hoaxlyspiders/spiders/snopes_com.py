from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import HoaxlyinboxschemaItem, PortiaItem


class Snopes(BasePortiaSpider):
    name = "snopes.com"
    allowed_domains = ['www.snopes.com', 'snopes.com']
    start_urls = ['http://snopes.com/']
    rules = [
        Rule(
            LinkExtractor(
                allow=('^https\\:\\/\\/snopes\\.com\\/fact\\-check'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                HoaxlyinboxschemaItem,
                None,
                'span:nth-child(5), .rating-wrapper',
                [
                    Field(
                        'factoidHeadline',
                        '.article-title *::text',
                        []),
                    Field(
                        'factoidContent',
                        '.entry-content > .article-text-inner *::text',
                        []),
                    Field(
                        'factoidClaim',
                        '.article-text-inner > p:nth-child(2) *::text',
                        []),
                    Field(
                        'factoidVerdict',
                        'span *::text',
                        []),
                    Field(
                        'factoidRating',
                        '.claim > img::attr(src)',
                        []),
                    Field(
                        'itemReviewed',
                        '.entry-content > .article-text-inner > p:nth-child(12) > a::attr(href)',
                        [])])]]
