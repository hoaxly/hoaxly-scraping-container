# Hoaxly development setup



## use portia
http://hoaxly.docksal:9001

### Start a crawl with portia
```
docker exec  hoaxly_portia_1 portiacrawl add /app/slybot/bin/portiacrawl <PROJECT_PATH> [SPIDER] [OPTIONS]
```

## use kibana
http://hoaxly.docksal:5601


### Show all content of index in kibana dev tools:
```
GET /hoaxly/_search?size=1000
```