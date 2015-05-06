# -*- coding: utf-8 -*-
import scrapy

from tslspyder.items import CancionItem

class YosiSpider(scrapy.Spider):
    name = "yosi"
    allowed_domains = ["http://yosisideral.emisorasunidas.com/20estrellas"]
    start_urls = (
        'http://yosisideral.emisorasunidas.com/20estrellas/',
    )

    def parse(self, response):
        
        for sel in response.xpath('//div/p'):
            item = CancionItem() 
            item['cancion'] = sel.xpath('text()').extract
            
            yield item 
