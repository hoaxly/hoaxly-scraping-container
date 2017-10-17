# Automatically created by: slyd
import os

#SPIDER_MANAGER_CLASS = 'slybot.spidermanager.ZipfileSlybotSpiderManager'
#SPIDER_LOADER_CLASS = 'slybot.spidermanager.ZipfileSlybotSpiderManager'
SPIDER_LOADER_CLASS = 'slybot.spidermanager.SlybotSpiderManager'
EXTENSIONS = {'slybot.closespider.SlybotCloseSpider': 10}
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

SPIDER_MIDDLEWARES = {
    # the one mounted in docker
    'slybot.mymiddleware.MicrodataExtruction': 643,
    # the one deployed as egg
    #'spiders.MicrodataExtruction': 643,

    'slybot.spiderlets.SpiderletsMiddleware': 999
}

ITEM_PIPELINES = {
    'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 600,

    # the one deployed as egg
    #'spiders.TypePipeline': 500,
    # the one mounted in docker
    'slybot.mypipelines.TypePipeline': 2,
    'slybot.dupefilter.DupeFilterPipeline': 1
}

ELASTICSEARCH_SERVERS = ['http://elastic:changeme@elastic:9200']
ELASTICSEARCH_INDEX = 'hoaxly'
ELASTICSEARCH_TYPE = 'items'
ELASTICSEARCH_UNIQ_KEY = 'url'
ELASTICSEARCH_INDEX_DATE_FORMAT = '%Y-%m'

# ugly but hardcoding works
PROJECT_DIR = '/app/data/projects/hoaxlyPortia'
#PROJECT_ZIPFILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

try:
    from local_slybot_settings import *
except ImportError:
    pass
