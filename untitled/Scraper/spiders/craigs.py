# -*- coding: utf-8 -*-
import scrapy


class CraigsSpider(scrapy.Spider):
    name = "craigs"
    allowed_domains = ["craigslist.org"]
    start_urls = ['http://craigslist.org/']

    def parse(self, response):
        pass
