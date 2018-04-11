# Automatically created by: slyd
import sys
import os
import hoaxlyHelpers
import scrapyelasticsearch
#import slybot
#SPIDER_LOADER_CLASS = 'slybot.spidermanager.ZipfileSlybotSpiderManager'
SPIDER_LOADER_CLASS = 'slybot.spidermanager.SlybotSpiderManager'

EXTENSIONS = {'slybot.closespider.SlybotCloseSpider': 1}

DOWNLOADER_MIDDLEWARES = {
    'slybot.pageactions.PageActionsMiddleware': 700,
    'slybot.splash.SlybotJsMiddleware': 725
}
PLUGINS = [
    'slybot.plugins.scrapely_annotations.Annotations',
    'slybot.plugins.selectors.Selectors'
]
SLYDUPEFILTER_ENABLED = True
#DUPEFILTER_CLASS = 'scrapy.dupefilters.RFPDupeFilter'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
DUPEFILTER_DEBUG = True
SPLASH_COOKIES_DEBUG = True
SPIDER_MIDDLEWARES = {
    'hoaxlyHelpers.mymiddleware.MicrodataExtruction': 1003,
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
    'slybot.spiderlets.SpiderletsMiddleware': 999
}

ITEM_PIPELINES = {
    #'hoaxlyHelpers.mypipelines.TypePipeline': 700,
    #'hoaxlyHelpers.indexpipeline.IndexPipeline': 800,
    'slybot.dupefilter.DupeFilterPipeline': 1,
    #'scrapy.dupefilters.DupeFilterPipeline': 100,
    'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 900
}

ELASTICSEARCH_SERVERS = ['http://elastic:changeme@hoaxly-storage-container:9200']
ELASTICSEARCH_INDEX = 'hoaxly'
ELASTICSEARCH_TYPE = 'items'
ELASTICSEARCH_UNIQ_KEY = 'url'
ELASTICSEARCH_INDEX_DATE_FORMAT = '%Y-%m'

# ugly but hardcoding works
#PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PROJECT_DIR = '/app/data/projects/hoaxlyPortia'
#PROJECT_ZIPFILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


# Polite Scraping
# see https://blog.scrapinghub.com/2016/08/25/how-to-crawl-the-web-politely-with-scrapy/
#
ROBOTSTXT_OBEY = True

USER_AGENT = 'Hoaxly Factchecking Search engine bot (bot@hoax.ly)'
# 55 second delay
DOWNLOAD_DELAY = 55.0

# https://doc.scrapy.org/en/latest/topics/autothrottle.html?
AUTOTHROTTLE_ENABLED = True
HTTPCACHE_ENABLED = False

# limit concurrent requests per domain
CONCURRENT_REQUESTS_PER_DOMAIN = 7

try:
    from local_slybot_settings import *
except ImportError:
    pass
