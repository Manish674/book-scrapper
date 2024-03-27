#!/usr/bin/env python3
from pathlib import Path

import scrapy


'''
byjus.com
links -> response.css("table tr td a::attr(href)").getall()
text -> response.css("table tr td a::attr(href)").getall()
'''

class quote_spider(scrapy.Spider):
    name = "books"
    allowed_domains = ["byjus.com"]
    start_urls = [
        "https://byjus.com/ncert-books"
    ]

    def parse(self, response):
        book_download_links = response.css("table tr td a::attr(href)").getall()
        book_titles = response.css("table tr td a::text").getall()

        book = {}

        for n in range(len(book_titles)):
            book[book_titles[n]] = book_download_links[n]

        unused_links = []
        len_unused_links = len(book_download_links) - len(book_titles)

        for n in range(-1, len_unused_links, 1):
            unused_links.append(book_download_links[n])

        yield {
            "books": book,
            "unused links": unused_links,
        }
