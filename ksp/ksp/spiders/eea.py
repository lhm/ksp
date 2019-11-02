# -*- coding: utf-8 -*-
import scrapy


class EeaSpider(scrapy.Spider):
    name = 'eea'
    allowed_domains = ['european-energy-award.de']
    start_urls = ['https://www.european-energy-award.de/kommunen/liste-der-eea-kommunen/']

    def parse(self, response):
        rows = response.css('tr.wtdirectory_all')
        for row in rows:
            yield self.parse_row(row)

    def parse_row(self, row):
        def extract(cell, query):
            return cell.css(query).get(default='').strip()

        cells = row.css('td')

        return {
            'name': extract(cells[2], 'span::text'),
            'postcode': extract(cells[3], 'td::text'),
            'state': extract(cells[4], 'td::text'),
            'eea-status': extract(cells[6], 'td::text'),
            'homepage': extract(cells[7], 'a::attr(href)'),
            'eea-url': extract(cells[8], 'a::attr(href)')
        }
