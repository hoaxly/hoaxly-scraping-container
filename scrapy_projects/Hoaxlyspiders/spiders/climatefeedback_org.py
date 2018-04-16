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


class ClimatefeedbackOrg(BasePortiaSpider):
    name = "climatefeedback.org"
    allowed_domains = ['climatefeedback.org']
    start_urls = ['https://climatefeedback.org/claim-reviews/',
                  {'type': 'generated',
                   'url': 'https://climatefeedback.org/claim-reviews/[2-4]',
                   'fragments': [{'type': 'fixed',
                                  'value': 'https://climatefeedback.org/claim-reviews/',
                                  'valid': True},
                                 {'type': 'range',
                                  'value': '2-4',
                                  'valid': True}]}]
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
                        'header > .entry-title *::text',
                        []),
                    Field(
                        'factoidContent',
                        '.entry-content *::text',
                        []),
                    Field(
                        'factoidSummary',
                        '.fact-check-card *::text',
                        []),
                    Field(
                        'factoidClaim',
                        '.entry-content > .fact-check-card > .fact-check-card__row > div:nth-child(2) *::text',
                        []),
                    Field(
                        'factoidVerdict',
                        '.entry-content > .fact-check-card > .fact-check-card__row > div:nth-child(3) *::text',
                        []),
                    Field(
                        'factoidRating',
                        '.fact-check-card__row__verdict__img::attr(src)',
                        []),
                    Field(
                        'factoidSourceUrls',
                        '.fact-check-card__details__text > a::attr(href)',
                        []),
                    Field(
                        'factoidTags',
                        '.bot-tag > a::attr(href)',
                        []),
                    Field(
                        'factoidPubdate',
                        'p:nth-child(3) *::text',
                        [])])]]
