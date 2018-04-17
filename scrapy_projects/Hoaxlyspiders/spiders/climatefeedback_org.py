from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem, HoaxlyinboxschemaItem, ItemreviewedItem


class ClimatefeedbackOrg(BasePortiaSpider):
    name = "climatefeedback.org"
    allowed_domains = ['climatefeedback.org']
    start_urls = ['https://climatefeedback.org/claim-reviews/',
                  {'url': 'https://climatefeedback.org/claim-reviews/[2-4]',
                   'fragments': [{'value': 'https://climatefeedback.org/claim-reviews/',
                                  'valid': True,
                                  'type': 'fixed'},
                                 {'value': '2-4',
                                  'valid': True,
                                  'type': 'range'}],
                   'type': 'generated'}]
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
                ItemreviewedItem,
                'itemReviewed',
                'span.fact-check-card__details__text > a:nth-child(3)',
                [
                    Field(
                        '957a-4a8e-9a89',
                        'header > .entry-title *::text',
                        []),
                    Field(
                        '7dd4-41ea-857d',
                        '.entry-content *::text',
                        []),
                    Field(
                        '2c4e-415e-a6a5',
                        '.entry-content > .fact-check-card > .fact-check-card__row > div:nth-child(2) > div:nth-child(2) *::text',
                        []),
                    Field(
                        '1e1b-498a-b66a',
                        '.entry-content > .fact-check-card > .fact-check-card__row > div:nth-child(3) > div:nth-child(2) > .fact-check-card__row__verdict__img::attr(src)',
                        []),
                    Field(
                        'd4cf-419d-ab88',
                        '.bot-tag > a::attr(href)',
                        []),
                    Field(
                        '9316-4a62-a60a',
                        '.main > p:nth-child(3) *::text',
                        []),
                    Field(
                        '3a3d-41b8-8eb2',
                        '.expert-widget > .wid-body *::text',
                        [])])]]
