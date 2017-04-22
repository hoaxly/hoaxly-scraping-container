
ITEM_PIPELINES = {
    'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 200,
    'slybot.pipelines.TypePipeline': 100,
    }


ELASTICSEARCH_SERVERS = ['http://elastic:9200']
ELASTICSEARCH_INDEX = 'hoaxly'
ELASTICSEARCH_TYPE = 'items'
ELASTICSEARCH_UNIQ_KEY = 'url'

