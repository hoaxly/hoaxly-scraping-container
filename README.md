
# Table of Contents

1.  [Setup](#org6e8aa9c)
    1.  [Step 1: Fetch the images](#org38d359a)
    2.  [Step 2: Spin up the local instances and initialize them.](#org0cfadc9)

A spider describes what data to get from where. You can write scrapy spiders in python code or you can use a tool like Portia.
Portia is an abstraction layer on top of scrapy that provides a UI in the browser for creating spiders.
Portia spiders can be exported in two ways (portia and scrapy)
This is a portia spiders collection for crawling websites and scraping content.

A running spider is called a crawler.
A spider crawl can be triggered manually to fetch data once or scheduled to crawl on a regular basis to fetch
data continuously. During a crawl the spider retrieves data and outputs it to a target (stdout, json files etc.)


<a id="org6e8aa9c"></a>

# Setup

<span class="underline">Requirements:</span>

-   docker-2.3.0
-   docker-compose-1.13.0

<span class="underline">Note:</span> make sure to run this on your host.
This is needed for elasticsearch to work [4]

    sudo sysctl -w vm.max_map_count=262144


<a id="org38d359a"></a>

## Step 1: Fetch the images

Login to our registry (using your gitlab credentials) to get at the images that you need in order to locally build and run spiders.

    docker login registry.acolono.net:444
    docker pull registry.acolono.net:444/hoaxly/hoaxly-storage-container
    docker pull registry.acolono.net:444/hoaxly/hoaxly-scrapydaemon-container
    docker pull registry.acolono.net:444/hoaxly/hoaxly-scraping-container


<a id="org0cfadc9"></a>

## Step 2: Spin up the local instances and initialize them.

In your project's rootfolder, run:

    fin init

Open your preferred browser and go to: http://portia.hoaxly.docksal

