from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class Snopes(BasePortiaSpider):
    name = "www.snopes.com"
    allowed_domains = [u'www.snopes.com']
    start_urls = [u'http://www.snopes.com/category/facts/']
    rules = [
        Rule(
            LinkExtractor(
                allow=(),
                deny=(
                    u'/whats-new/',
                    u'/50-hottest-urban-legends/',
                    u'/news/',
                    u'/video/',
                    u'/frequently-asked-questions/',
                    u'/glossary/',
                    u'/archive/')),
            callback='parse_item',
            follow=True)]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'.body-content',
                [
                    Field(
                        u'category',
                        u'.breadcrumb-nav > a:nth-child(2)::attr(href)',
                        []),
                    Field(
                        u'title',
                        u'.article-title *::text',
                        []),
                    Field(
                        u'subtitle',
                        u'.article-description *::text',
                        []),
                    Field(
                        u'claimText',
                        u'.entry-content > p:nth-child(2) *::text',
                        []),
                    Field(
                        u'ratingImage',
                        u'.entry-content > .false > img::attr(src)',
                        []),
                    Field(
                        u'researcher',
                        u'.author-box  .author-link::attr(href)',
                        [
                            Url()]),
                    Field(
                        u'editDate',
                        u'.entry-content > .article-footer > .article-info-box > p:nth-child(4) > .date-wrapper *::text',
                        []),
                    Field(
                        u'sources',
                        u'.entry-content > .article-footer > .article-sources-box *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.body-content',
                [
                    Field(
                        u'Category',
                        u'.breadcrumb-nav > a:nth-child(2)::attr(href)',
                        []),
                    Field(
                        u'Headline',
                        u'header > .article-title::attr(itemprop)',
                        []),
                    Field(
                        u'title',
                        u'.article-title *::text',
                        []),
                    Field(
                        u'subtitle',
                        u'header > .article-description *::text',
                        []),
                    Field(
                        u'altname',
                        u'.entry-content > span:nth-child(4) > span::attr(itemprop)',
                        []),
                    Field(
                        u'fact_rating',
                        u'.entry-content > .false *::text',
                        []),
                    Field(
                        u'Researcher',
                        u'.author-box > .author-link::attr(href)',
                        []),
                    Field(
                        u'pubDate',
                        u'.entry-content > .article-footer > .article-info-box > p:nth-child(3) > .date-wrapper *::text',
                        []),
                    Field(
                        u'sources',
                        u'.entry-content > .article-footer > .article-sources-box *::text',
                        []),
                    Field(
                        u'complete_meta',
                        u'.has-featured-video::attr(itemtype)',
                        [])])]]
