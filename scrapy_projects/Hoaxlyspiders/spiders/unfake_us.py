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


class UnfakeUs(BasePortiaSpider):
    name = "unfake.us"
    allowed_domains = ['unfake.us']
    start_urls = ['https://unfake.us/articles/?activity=annotations&website=']
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
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
                '.article-page',
                [
                    Field(
                        'factoidHeadline',
                        'div:nth-child(1) > h1 > a::attr(href)',
                        []),
                    Field(
                        'factoidClaim',
                        '.row > .col-md-8 > div:nth-child(1) > .summary > p *::text',
                        []),
                    Field(
                        'itemReviewed',
                        '.row > .col-md-8 > div:nth-child(1) > .summary > a:nth-child(4)::attr(href)',
                        []),
                    Field(
                        'factoidRating',
                        '.row > .col-md-8 > .contribution > .content > h3 > .tag > span *::text',
                        []),
                    Field(
                        'factoidVerdict',
                        '.row > .col-md-8 > .contribution > .content > .text *::text',
                        []),
                    Field(
                        'claimReviewers',
                        '.row > .col-md-4 > div > ul:nth-child(4) > li > a::attr(href)',
                        [])])]]
