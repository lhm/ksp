# -*- coding: utf-8 -*-
import scrapy

class Mp100Spider(scrapy.Spider):
    name = 'mp100'
    allowed_domains = ['klimaschutz.de']
    start_urls = ['https://www.klimaschutz.de/masterplan-kommunen-liste']

    def parse(self, response):
        # follow links to project pages
        for href in response.css('.views-field-title a::attr(href)'):
            yield response.follow(href, self.parse_details)

        # follow pagination links
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_details(self, response):
        infobox = response.css('div.group-projectinformation')
        def extract(query):
            return infobox.css(query).get(default='').strip()

        yield {
            'name': extract('.field-name-field-project-initiator .field-item::text'),
            'url': extract('.field-name-field-project-applicant-contact a::attr(href)'),
            'grant_id': extract('.field-name-field-project-support-id .field-item::text'),
            'source': response.url
        }
