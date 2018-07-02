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


class CorrectivOrg(BasePortiaSpider):
    name = "correctiv.org"
    allowed_domains = ['correctiv.org']
    start_urls = [
        'https://correctiv.org/echtjetzt/']
    rules = [
        Rule(
            LinkExtractor(
                allow=('^https\\:\\/\\/correctiv\\.org\\/echtjetzt\\/artikel\\/'),
                deny=()),
            callback='parse_item',
            follow=True)]
    items = [
        [
            Item(
                HoaxlyinboxschemaItem,
                None,
                '#entry-2578',
                [
                    Field(
                        'factoidHeadline',
                        '.article-header > .article-header__headline-group > .article-header__headline *::text',
                        []),
                    Field(
                        'claimReviewers',
                        '.article-body > .article-body__aside > .vcard > .fn::attr(href)',
                        []),
                    Field(
                        'factoidPubdate',
                        '.article-body > .article-body__aside > .article-body__publishing-date *::text',
                        []),
                    Field(
                        'factoidContent',
                        '.article-body > .article-body__main *::text',
                        []),
                    Field(
                        'itemReviewed',
                        '.article-body > .article-body__main > p:nth-child(1) > a::attr(href)',
                        []),
                    Field(
                        'factoidClaim',
                        '.article-body__main > p:nth-child(2) *::text',
                        []),
                    Field(
                        'factoidVerdict',
                        '.article-body > .article-body__claimreview > .claimreview__title *::text',
                        []),
                    Field(
                        'factoidRating',
                        '.article-body > .article-body__claimreview > .claimreview__picture::attr(src)',
                        []),
                    Field(
                        'factoidSourceUrls',
                        '.article-body__main > p:nth-child(4) > a::attr(href)',
                        [])])]]
