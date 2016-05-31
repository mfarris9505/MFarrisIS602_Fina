# -*- coding: utf-8 -*-
"""
Created on Tue May 17 18:26:33 2016

@author: Matts42
"""
import scrapy
from scrapy.spiders import CrawlSpider
#from scrapy.linkextractors import LinkExtractor

from lyric.items import Lyric_Item
class MySpider(CrawlSpider):

    name = 'lyric'
    allowed_domains = ['http://lyrics.wikia.com/']
    start_urls = ['http://lyrics.wikia.com/wiki/Special:Random']


    def parse(self, response):
        global x 
        lyric = Lyric_Item()
        lyric['title_name'] = response.xpath('//h1').extract()
        lyric['lyric'] = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "lyricbox", " " ))]').extract()
        yield lyric
        
        url = "http://lyrics.wikia.com/wiki/Special:Random"
        yield scrapy.Request(url, callback = self.parse)

    
    
