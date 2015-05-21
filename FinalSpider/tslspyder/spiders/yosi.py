# -*- coding: utf-8 -*-
import scrapy
import re

from tslspyder.items import CancionItem

class YosiSpider(scrapy.Spider):
    name = "yosi"
    allowed_domains = ["http://yosisideral.emisorasunidas.com/20estrellas"]
    start_urls = (
        'http://yosisideral.emisorasunidas.com/20estrellas/',
    )

    def parse(self, response):
        
         for sel in response.xpath('//div/div/div/div/div/ul/li/div/div'):
            item = CancionItem() 
            temp = sel.xpath('p[contains(@class, "top-song")]/text()').extract();
            if len(temp) > 0:
                temp1 = temp[0];
                tre = re.compile('^\d+\. ');
                item['cancion'] = tre.sub('',temp1).strip();
                item['artista'] = sel.xpath('p[contains(@class, "top-autor")]/text()').extract();
                item['disco'] = sel.xpath('p[contains(@class, "top-disco")]/text()').extract();
                
                
            
                if item['cancion']:
                    yield item 
