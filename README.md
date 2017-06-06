# Hoaxly development environment

this repo contains:

- a docksal setup - _basically a docker-compose.yml file and an init script.
- portia spiders - _portia spiders are basically scrapy spiders with bells on.
- some configuration - _the file at config/local_slybot_settings.py will be mounted in the portia container allowing us to configure it. it is loaded by https://github.com/scrapinghub/portia/blob/master/slybot/slybot/settings.py
- custom spider middleware. - portia_projects/hoaxlyPortia/spidermiddleware.py registering classes defined in this file in our configuration allows interacting with the data before pipelines kick in_


## Requirements

docker-2.3.0 docker-compose-1.13.0


## Setup

from projectroot run

    ☻ % docker-compose -f docksal.yml pull --parallel
    ☻ % fin init

this will spin up your containers defined in .docksal/docksal.yml

## use portia

in your browser you can visit the [webinterface of portia](http://hoaxly.docksal:9001)
you will find the hoaxlyPortia project containing some spiders.

you can view your spiders in your file browser at portia_projects/hoaxlyPortia/spiders

for more details see

- https://doc.scrapy.org/en/latest/index.html
- http://scrapyd.readthedocs.io/en/latest/
- http://portia.readthedocs.io/en/latest/index.html

### Start a crawl with portia
http://portia.readthedocs.io/en/latest/spiders.html#running-a-spider
you will get a list of spiders if you run this command

    docker exec hoaxly_portia_1  <PROJECT_PATH> [SPIDER] [OPTIONS]
    docker exec hoaxly_portia_1 portiacrawl /app/data/projects/hoaxlyPortia


## deploy to scrapyd

  ☻ % docker exec -ti hoaxly_portia_1 bash
  root@3d4a705434fb:/app/data/projects/hoaxlyPortia# scrapyd-deploy -a

## Elasticsearch via scrapyelasticsearch
we are using the following fork of the python library
https://github.com/suraj-arya/scrapy-elasticsearch
activating and configuring the pipeline in our settings is enough to get the data saved (infact we still have a workaround in place that renames an items "_type" key to "type" to avoid elastic search error)

## use kibana
http://hoaxly.docksal:5601

default index: hoaxly
(uncheck contains timedata)

## basic php frontend for elasticsearch
  search.hoaxly.docksal

## Custom Middleware
Spider middleware for enriching item with scraped metadata

    portia_projects/hoaxlyPortia/spidermiddleware.py

https://doc.scrapy.org/en/latest/topics/spider-middleware.html#scrapy.spidermiddlewares.SpiderMiddleware.process_spider_output
