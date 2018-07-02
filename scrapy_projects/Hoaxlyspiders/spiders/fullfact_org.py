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


class FullfactOrg(BasePortiaSpider):
    name = "fullfact.org"
    allowed_domains = ['fullfact.org']
    start_urls = ['https://fullfact.org/']
    rules = [
        Rule(
            LinkExtractor(
                allow=(),
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
                'blockquote > p:nth-child(2)',
                [
                    Field(
                        'factoidHeadline',
                        '.header > h1 *::text',
                        []),
                    Field(
                        'factoidPubdate',
                        '.date *::text',
                        []),
                    Field(
                        'factoidContent',
                        '.article-post-content > .row > .col-xs-12 *::text',
                        []),
                    Field(
                        'factoidClaim',
                        '.box-panel > div > .col-left > p *::text, .box-panel > div > .inner-row > .col-left > p *::text',
                        []),
                    Field(
                        'factoidVerdict',
                        '.box-panel > div > div > p *::text, .box-panel > div > div > .col-right > p *::text',
                        []),
                    Field(
                        'claimSource',
                        '.article-post-content > .row > .col-xs-12 > div:nth-child(2) > blockquote *::text',
                        []),
                    Field(
                        'itemReviewed',
                        'a::attr(href)',
                        []),
                    Field(
                        'claimReviewers',
                        '.article-post-content > .row > .col-xs-12 > div:nth-child(2) > .post-content-footer-author *::text',
                        [])])]]
