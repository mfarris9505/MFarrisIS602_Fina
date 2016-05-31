# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from movies.items import Movie_Item

class Movie_Spider(CrawlSpider):
    name = "movie"
    allowed_domains = ["imdb.com"]
    start_urls = (
        'http://www.imdb.com/title/tt0120815/reviews?start=0',
    )

    def parse(self, response):
        for rev in response.xpath('//*[(@id = "tn15content")]'):
            item = Movie_Item()
            item['review'] = rev.xpath('//p').extract()
            item['rating'] = rev.xpath('//h2+//img').extract()
            yield item
        next_page = response.css("td img")
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)
