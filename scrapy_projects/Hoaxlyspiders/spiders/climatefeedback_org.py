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
    start_urls = ['https://climatefeedback.org/claimreview/rush-limbaugh-falsely-claims-there-is-no-evidence-of-human-caused-global-warming/',
                  {'fragments': [{'valid': True,
                                  'type': 'fixed',
                                  'value': 'https://climatefeedback.org/claim-reviews/'},
                                 {'valid': True,
                                  'type': 'range',
                                  'value': '2-4'}],
                      'url': 'https://climatefeedback.org/claim-reviews/[2-4]',
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
                HoaxlyinboxschemaItem,
                None,
                '.main',
                [
                    Field(
                        'itemReviewed',
                        '.entry-content > .fact-check-card > div:nth-child(2) > .mb2 > p > .fact-check-card__details__text > a:nth-child(3) > .fa::attr(aria-hidden)',
                        [],
                        True),
                    Field(
                        'factoidHeadline',
                        '.entry-title *::text',
                        [],
                        True),
                    Field(
                        'factoidContent',
                        '.entry-content *::text',
                        []),
                    Field(
                        'factoidClaim',
                        '.entry-content > .fact-check-card > .fact-check-card__row > div:nth-child(2) *::text',
                        []),
                    Field(
                        'factoidRating',
                        '.entry-content > .fact-check-card > .fact-check-card__row > div:nth-child(3) > div:nth-child(2) > .fact-check-card__row__verdict__img::attr(src)',
                        []),
                    Field(
                        'factoidTags',
                        '.content > .main > .spaceup1 > .bot-tag > a::attr(href)',
                        []),
                    Field(
                        'factoidPubdate',
                        'p:nth-child(3) *::text',
                        []),
                    Field(
                        'claimReviewers',
                        '.content > .sidebar > .widget-last > .textwidget > .row *::text',
                        [
                            Image(),
                            Text()])])]]
