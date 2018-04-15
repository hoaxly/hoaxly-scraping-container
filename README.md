
# Table of Contents

1.  [Setup](#org67020e2)
    1.  [step 1 is to fetch the images](#orgafe844e)
    2.  [Step 2 is to spin up the local instances and initialize them.](#orgde9a677)

portia is an abstraction layer on top of scrapy.
that provides a ui in the browser for orchestrating spiders, portia spiders can be exported in two ways

is a portia spiders collection for crawling websites and scraping content.

-   **we create some code and call it a spider:** a spider describes what data to get from where

You can write scrapy spiders in python code or you can use a service like portia (portia can be selfhosted
or used on saas platform scrapycloud/hub) to build your spider in the browser and export. Portia provides you with
an additional abstraction layer on top of scrapy.

A running spider is called a crawler.
running a spider to scrape the data we care about from a source
A spider crawl can be triggered manually to fetch data once or schedule a spider to crawl on a regular basis to fetch
data continuously.
During a crawl the spider retrieves data and outputs it to a target (stdout, json files etc.)


<a id="org67020e2"></a>

# Setup

Requirements

docker-2.3.0 docker-compose-1.13.0

<span class="underline">Note:</span> make sure to run this on your host.
This is needed for elasticsearch to work [4]

    sudo sysctl -w vm.max_map_count=262144


<a id="orgafe844e"></a>

## step 1 is to fetch the images

login to our registry if you have access to get at the images you need to locally build and run spiders.

    docker login registry.acolono.net:444
    docker pull registry.acolono.net:444/hoaxly/hoaxly-storage-container
    docker pull registry.acolono.net:444/hoaxly/hoaxly-scrapydaemon-container
    docker pull registry.acolono.net:444/hoaxly/hoaxly-scraping-container


<a id="orgde9a677"></a>

## Step 2 is to spin up the local instances and initialize them.

from projectroot run

    fin init

