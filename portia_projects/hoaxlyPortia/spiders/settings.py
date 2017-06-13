# Automatically created by: slyd
import os

SPIDER_LOADER_CLASS = 'slybot.spidermanager.SlybotSpiderManager'
EXTENSIONS = {'slybot.closespider.SlybotCloseSpider': 1}
ITEM_PIPELINES = {'slybot.dupefilter.DupeFilterPipeline': 1}
# as close as possible to spider output
SPIDER_MIDDLEWARES = {'slybot.spiderlets.SpiderletsMiddleware': 999}
DOWNLOADER_MIDDLEWARES = {
    'slybot.pageactions.PageActionsMiddleware': 700,
    'slybot.splash.SlybotJsMiddleware': 725
}
PLUGINS = [
    'slybot.plugins.scrapely_annotations.Annotations',
    'slybot.plugins.selectors.Selectors'
]
SLYDUPEFILTER_ENABLED = True
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

ITEM_PIPELINES = {
    'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 200,
    'pipelines.TypePipeline': 100,
}

SPIDER_MIDDLEWARES = {
    'spidermiddleware.MicrodataExtruction': 543
}

ELASTICSEARCH_SERVERS = ['http://elastic:9200']
ELASTICSEARCH_INDEX = 'hoaxly'
ELASTICSEARCH_TYPE = 'items'
ELASTICSEARCH_UNIQ_KEY = 'url'


try:
    from local_slybot_settings import *
except ImportError:
    pass
