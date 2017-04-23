"""
Custom settings for hoaxlyPortia

"""
import sys
sys.path.append('/app/data/projects/hoaxlyPortia')

SPIDER_MIDDLEWARES = {
    'spidermiddleware.MicrodataExtruction': 543,
}


ITEM_PIPELINES = {
    'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 200,
    'pipelines.TypePipeline': 100,
}

ELASTICSEARCH_SERVERS = ['http://elastic:9200']
ELASTICSEARCH_INDEX = 'hoaxly'
ELASTICSEARCH_TYPE = 'items'
ELASTICSEARCH_UNIQ_KEY = 'url'
