#!/usr/bin/env python3
from pathlib import Path

import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        "https://quotes.toscrape.com/page/2/",
    ]

    def parse(self, response):

        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text"),
                "author": quote.css("span.author::text"),
                "tags": quote.css("div.tags a.tag::text")
            }
