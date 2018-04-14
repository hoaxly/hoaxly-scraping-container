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


class ClimatefeedbackOrg(BasePortiaSpider):
    name = "climatefeedback.org"
    allowed_domains = ['climatefeedback.org']
    start_urls = ['https://climatefeedback.org/claim-reviews/']
    rules = [
        Rule(
            LinkExtractor(
                allow=('/claimreview/'),
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
                '.main',
                [
                    Field(
                        'factoidHeadline',
                        '.post-7296 > header > .entry-title *::text',
                        []),
                    Field(
                        'factoidSummary',
                        '.post-7296 > .entry-content > .fact-check-card *::text',
                        []),
                    Field(
                        'factoidClaim',
                        '.post-7296 > .entry-content > .fact-check-card > .fact-check-card__row > div:nth-child(2) *::text',
                        []),
                    Field(
                        'factoidVerdict',
                        '.post-7296 > .entry-content > .fact-check-card > .fact-check-card__row > div:nth-child(3) *::text',
                        []),
                    Field(
                        'factoidSourceUrls',
                        '.post-7296 > .entry-content > .fact-check-card > div:nth-child(2) > .mb2 > p > .fact-check-card__details__text > a:nth-child(2)::attr(href)',
                        []),
                    Field(
                        'factoidPubdate',
                        'p:nth-child(3) *::text',
                        [])])]]
