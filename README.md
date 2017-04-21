# Hoaxly development setup

## use portia

using the newest dev in docker requires us to build it ourselves.

from projectroot run

    build_portia

then you can run 

    fin init


http://hoaxly.docksal:9001

### Start a crawl with portia
```
docker exec hoaxly_portia_1  <PROJECT_PATH> [SPIDER] [OPTIONS]

docker exec hoaxly_portia_1 portiacrawl /app/data/projects/hoaxlyPortia
```

## use kibana
http://hoaxly.docksal:5601

### Create Index

POST hoaxly
### Show all content of index in kibana dev tools:
```
GET /hoaxly/_search?size=1000
```