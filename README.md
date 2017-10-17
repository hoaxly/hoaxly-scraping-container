# Hoaxly Portia spiders


!!!


scrapy crawl -s PROJECT_DIR=./ -s SPIDER_MANAGER_CLASS=slybot.spidermanager.SlybotSpiderManager snopes.com


!!!

## Requirements

    docker-2.3.0 docker-compose-1.13.0


## TLDR

from projectroot run

    ☻ % fin init
    ☻ % docker exec portia scrapyd &
    ☻ % docker exec -ti portia /bin/bash
    
then you are in container and can

    root@9e8c8aa1b4c2:/app/slyd# cd /app/data/projects/hoaxlyPortia/
    root@9e8c8aa1b4c2:/app/data/projects/hoaxlyPortia# scrapy-client deploy
    root@9e8c8aa1b4c2:/app/data/projects/hoaxlyPortia# scrapy-client schedule -p HoaxlyPortia snopes.com
    
and view your results:

    http://localhost:9200/hoaxly/_search

## Setup (Detailed)

this will spin up your containers defined in .docksal/docksal.yml
check that all containers are Up via


    ☻ % fin ps

Disable XPACK:

```
    ☻ docker exec hoaxly_elastic_1 bin/elasticsearch-plugin remove x-pack
    ☻ docker exec hoaxly_kibana_1 bin/kibana-plugin remove x-pack
    ☻ fin restart     
```



## components
this repo contains:


|     component    | Description           |
| ------------- |:-------------:|
| a docksal setup      | basically a docker-compose.yml file and an init script|
| portia spiders       | portia spiders are basically scrapy spiders with bells on      |
| some configuration   | the file at config/local_slybot_settings.py will be mounted in the portia container allowing us to configure it. it is loaded by https://github.com/scrapinghub/portia/blob/master/slybot/slybot/settings.py      |  
|custom spider middleware|portia_projects/hoaxlyPortia/spidermiddleware.py registering classes defined in this file in our configuration allows interacting with the data before pipelines kick in|



### Portia Spiders:

in your browser you can visit the [webinterface of portia](http://localhost:9001) use this to build new spiders

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

_Note:_ make sure to run this on your host

    ☻ % sudo sysctl -w vm.max_map_count=262144

needed for elasticsearch to work [4]    


[2]: https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-cli-run-prod-mode
[3]: https://github.com/suraj-arya/scrapy-elasticsearch
[4]: https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html


### scrapyd

- https://doc.scrapy.org/en/latest/index.html
- http://scrapyd.readthedocs.io/en/latest/

    root@0ee451559ce0:/app/data/projects/hoaxlyPortia# scrapy crawl snopes.com

    docker exec portia scrapyd


#### Deploy to scrapyd and scheduling crawls using [scrapyd-client](https://github.com/scrapy/scrapyd-client)

    ☻ % docker exec -ti portia bash
    root@87a89036ec31:/app/slyd# cd /app/data/projects/hoaxlyPortia
    root@3d4a705434fb:/app/data/projects/hoaxlyPortia# scrapyd-deploy -a
    
    scrapyd-client deploy

once deployed you can interact directly with scrapyd through the webapi

    scrapyd-client schedule -p hoaxlyPortia snopes.com
    scrapyd-client schedule
    curl http://localhost:6800/schedule.json -d project=HoaxlyPortia -d spider=www.theskepticsguide.org
    curl http://localhost:6800/listprojects.json
    curl http://localhost:6800/listspiders.json?project=HoaxlyPortia


## basic php frontend demo for elasticsearch

    http://search.hoaxly.docksal/index.php
