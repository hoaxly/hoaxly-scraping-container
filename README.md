# Hoaxly Portia spiders


!!!


scrapy crawl -s PROJECT_DIR=./ -s SPIDER_MANAGER_CLASS=slybot.spidermanager.SlybotSpiderManager snopes.com


!!!

## Requirements

    docker-2.3.0 docker-compose-1.13.0


## TLDR

### To run spiders
_Note:_ make sure to run this on your host.
This is needed for elasticsearch to work [4]

    ☻ % sudo sysctl -w vm.max_map_count=262144

from projectroot run

    ☻ % fin init
    ☻ % docker exec -ti cli /bin/bash

then you are in container and can

    # cd /var/www/scrapy_projects/Hoaxlyspiders
    # scrapyd-client deploy local
    # scrapyd-client schedule -p HoaxlySpiders climatefeedback.org

and view your results:

    http://elastic.hoaxly.docksal:9200/hoaxly/_search



## Components

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

once you have some data scraped to elasticsearch enable this container and visit the [kibana web interface](http://localhost:5601) to inspect your index
default index: hoaxly
(uncheck contains timedata)

HINT: It may take some time (>5 min) and a huge amount of ram & cpu load to
restart kibana for the first time after disabling xpack, because some assets are
rebuild. To save some memory you can stop the elastic container until kibana is
ready again.


### Elastic:

view [elasticsearch webinterface](http://localhost:9200/) in the browser
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

    root@0ee451559ce0:/app/data/projects/hoaxlyPortia# scrapy crawl snopes.com

    docker exec portia scrapyd


#### Deploy to scrapyd and scheduling crawls using [scrapyd-client](https://github.com/scrapy/scrapyd-client)

    ☻ % docker exec -ti cli bash
    # scrapyd-deploy -a

    scrapyd-client deploy

once deployed you can interact directly with scrapyd through the webapi

    scrapyd-client schedule -p hoaxlyPortia snopes.com

or just run This

    curl http://scrapydaemon.hoaxly.docksal:6800/schedule.json -d project=Hoaxlyspiders -d spider=climatefeedback.org

    curl http://localhost:6800/schedule.json -d project=HoaxlyPortia -d spider=www.theskepticsguide.org
    curl http://localhost:6800/listprojects.json
    curl http://localhost:6800/listspiders.json?project=HoaxlyPortia


## basic php frontend demo for elasticsearch

    http://search.hoaxly.docksal/index.php
