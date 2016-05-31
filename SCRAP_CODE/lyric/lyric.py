# -*- coding: utf-8 -*-
"""
Created on Tue May 17 18:26:33 2016

@author: Matts42
"""

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MySpider(CrawlSpider):
    name = 'lyric'
    allowed_domains = ['http://lyrics.wikia.com/']
    start_urls = ['http://lyrics.wikia.com/wiki/Melissa_O%27Neil:Just_Like_January']
    
    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[contains(concat( " ", @class, " " ), concat( " ", "subnav-2a", " " ))]',)), callback="parse"),
    )
    
    def parse(self, response):
        lyric = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "lyricbox", " " ))]').extract()
        print lyric
    
    
 