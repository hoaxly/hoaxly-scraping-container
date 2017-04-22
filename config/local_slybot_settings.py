import sys
sys.path.append('/app/data/projects/hoaxlyPortia')


ITEM_PIPELINES = {
    'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 200,
    'pipelines.TypePipeline': 100,
    'spidermiddleware.MicrodataExtruction': 50,
}

SPIDER_MIDDLEWARES = {
    'spidermiddleware.MicrodataExtruction': 543,
}

ELASTICSEARCH_SERVERS = ['http://elastic:9200']
ELASTICSEARCH_INDEX = 'hoaxly'
ELASTICSEARCH_TYPE = 'items'
ELASTICSEARCH_UNIQ_KEY = 'url'