# Hoaxly Portia spiders


!!!


scrapy crawl -s PROJECT_DIR=./ -s SPIDER_MANAGER_CLASS=slybot.spidermanager.SlybotSpiderManager snopes.com


!!!

## Requirements

    docker-2.3.0 docker-compose-1.13.0


## TLDR
_Note:_ make sure to run this on your host.
This is needed for elasticsearch to work [4]

    ☻ % sudo sysctl -w vm.max_map_count=262144

from projectroot run

    ☻ % fin init

### Edit or create a spiders

1. visit portia.hoaxly.docksal
2. create or edit a spider in the HoaxlySpiders project
3. export to scrapy_projects as scrapy spider

### Deploy spiders via cli and schedule a run

    ☻ % docker exec -ti cli /bin/bash

then you are in the cli container and can

    root@9e8c8aa1b4c2:/app/slyd# cd /var/www/scrapy_projects/HoaxlySpiders
    root@9e8c8aa1b4c2:/app/data/projects/hoaxlyPortia# scrapyd-client deploy local
    root@9e8c8aa1b4c2:/app/data/projects/hoaxlyPortia# scrapyd-client schedule -p HoaxlyPortia climatefeedback.org

and view your results:

    http://elastic.hoaxly.docksal:9200/hoaxly/_search


## Production:

just pull the image from registry and run it, then you should see the projects spiders ready deployed and can schedule crawls through the api and watch the results show up in elasticsearch
mount the settings you need so scrapy knows where to pipe the data

## components



### Portia Spiders:

in your browser you can visit the [webinterface of portia](http://hoaxly.docksal:9001/#/projects) use this to build new spiders

Spiders are stored in [./portia_projects](./portia_projects)

we are using [Custom Spider middleware](https://doc.scrapy.org/en/latest/topics/spider-middleware.html#scrapy.spidermiddlewares.SpiderMiddleware.process_spider_output) for enriching item with scraped metadata

    portia_projects/hoaxlyPortia/spidermiddleware.py




#### Start a crawl with portia


you will get a list of spiders if you run this command [1]

    docker exec portia  <PROJECT_PATH> [SPIDER] [OPTIONS]
    docker exec portia portiacrawl /app/data/projects/hoaxlyPortia

for example try

    docker exec portia portiacrawl /app/data/projects/hoaxlyPortia www.snopes.com -o /app/data/example-output/snopes-output.json
    --settings=hoaxly
[1]: http://portia.readthedocs.io/en/latest/spiders.html#running-a-spider

### Kibana:

once you have some data scraped to elasticsearch enable this container and visit the [kibana web interface](http://kibana.hoaxly.docksal:5601) to inspect your index
default index: hoaxly
(uncheck contains timedata)

HINT: It may take some time (>5 min) and a huge amount of ram & cpu load to
restart kibana for the first time after disabling xpack, because some assets are
rebuild. To save some memory you can stop the elastic container until kibana is
ready again.


### Elastic:

view [elasticsearch webinterface](http://elastic.hoaxly.docksal:9200/) in the browser
uses a volume bound on /usr/share/elasticsearch/data [2]
Connects to Elasticsearch via scrapyelasticsearch python library [3]

activating and configuring the pipeline in our settings is enough to get the data saved
we still have a workaround in place that renames an items
> "\_type" key to "type"
to avoid elastic search error




[2]: https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-cli-run-prod-mode
[3]: https://github.com/suraj-arya/scrapy-elasticsearch
[4]: https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html


### scrapyd

- https://doc.scrapy.org/en/latest/index.html
- http://scrapyd.readthedocs.io/en/latest/

the scrapyd service runs in its own container


#### Deploy to scrapyd and scheduling crawls using [scrapyd-client](https://github.com/scrapy/scrapyd-client)

    ☻ % docker exec -ti cli bash
    root@87a89036ec31:/app/slyd# cd cd /var/www/scrapy_projects/HoaxlySpiders
    root@3d4a705434fb:/app/data/projects/hoaxlyPortia# scrapyd-deploy -a


once deployed you can interact directly with scrapyd through the webapi

    scrapyd-client schedule -p HoaxlySpiders climatefeedback.org

or from anywhere else with access to the scrapyd containers
    curl http://localhost:6800/schedule.json -d project=HoaxlyPortia -d spider=www.theskepticsguide.org
    curl http://localhost:6800/listprojects.json
    curl http://localhost:6800/listspiders.json?project=HoaxlyPortia


## basic php frontend demo for elasticsearch

    http://search.hoaxly.docksal/index.php
