# -*- coding: utf-8 -*-
import scrapy

from tslspyder.items import CancionItem

class AtmosferaSpider(scrapy.Spider):
    name = "atmosfera"
    allowed_domains = ["http://www.atmosfera.emisorasunidas.com/presionatmosferica"]
    start_urls = (
        'http://www.atmosfera.emisorasunidas.com/presionatmosferica/',
    )

    def parse(self, response):
        
        for sel in response.xpath('//div/p'):
            item = CancionItem() 
            item['cancion'] = sel.xpath('text()').extract
            
            yield item
