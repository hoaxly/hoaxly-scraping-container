# Hoaxly development setup

This container contains:

- Elasticsearch 5.2.2 (user: elastic, pass: changeme)
- Kibana for debugging (runs on http://localhost:5601, credentials from above)
- Scrapyd, with ScrapyElasticSearch and (with demo scraper for orf.at)

## Start a crawl of orf.at
```
fin bash scrapyd
cd /hoaxly/spiders/dirbot/
scrapy crawl orf --output=- --output-format=json
```

## Show all content of index in kibana dev tools:
```
GET /hoaxly/_search?size=1000
```