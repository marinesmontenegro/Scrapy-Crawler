# -*- coding: utf-8 -*-
import scrapy

from tslspyder.items import CancionItem

class A949Spider(scrapy.Spider):
    name = "949"
    allowed_domains = ["http:www.949.com.gt/pages/veinte_mas"]
    start_urls = (
        'http://www.949.com.gt/pages/veinte_mas/',
       
    )

    def parse(self, response):
        
        for sel in response.xpath('//div/div/div/div/ul/li/div/div/a/span'):
            item = CancionItem()
           
            
            temp = sel.xpath('text()').extract()[0];
            temp1 = temp.split(u'–');
            item['cancion'] = temp1[0].strip();
            item['artista'] = temp1[1].strip();
        
        
            yield item
            
 
