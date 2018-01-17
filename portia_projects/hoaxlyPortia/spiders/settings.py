# Automatically created by: slyd
import os
import hoaxlyHelpers
import scrapyelasticsearch
import slybot

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
SLYDUPEFILTER_ENABLED = False
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

SPIDER_MIDDLEWARES = {
    'hoaxlyHelpers.mymiddleware.MicrodataExtruction': 643,
    'slybot.spiderlets.SpiderletsMiddleware': 999
}

ITEM_PIPELINES = {
    'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 600,
    'hoaxlyHelpers.mypipelines.TypePipeline': 3,
    'slybot.dupefilter.DupeFilterPipeline': 700
}

ELASTICSEARCH_SERVERS = ['http://elastic:changeme@elastic:9200']
ELASTICSEARCH_INDEX = 'hoaxly'
ELASTICSEARCH_TYPE = 'items'
ELASTICSEARCH_UNIQ_KEY = 'url'
ELASTICSEARCH_INDEX_DATE_FORMAT = '%Y-%m'

# ugly but hardcoding works
PROJECT_DIR = '/app/data/projects/hoaxlyPortia'

try:
    from local_slybot_settings import *
except ImportError:
    pass
