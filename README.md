# Scraping Klimaschutzprogramme

Various scrapers for regional climate action plans ("Klimaschutzprogramme").

## Sources

* [European Energy Award](https://www.european-energy-award.de/)
* [Masterplan Kommunen](https://www.klimaschutz.de/masterplan-kommunen)

## Running

```
# list scrapers
$ docker-compose run scrapy list

# run a specific crawler and save the output in the data directory 
$ docker-compose run scrapy crawl eea -o /data/eea-participants.jl

# view data using jq
$ head -n1 data/eea-participants.jl | jq .
{
  "name": "Aachen",
  "postcode": "52064",
  "state": "Nordrhein-Westfalen",
  "eea-status": "Gold-zertifizierte Stadt / Gemeinde",
  "homepage": "http://www.aachen.de",
  "eea-url": "https://www.european-energy-award.de/kommunen/liste-der-eea-kommunen/details/eea/aachen/"
}

```

Caching is enabled and set to cache forever. Use the `-s HTTPCACHE_ENABLED=False` flag to override, or
change it in [the settings](ksp/ksp/settings.py)
