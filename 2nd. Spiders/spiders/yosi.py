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
        
        for sel in response.xpath('//div/div/div/div/div/ul/li/div/div'):
            item = CancionItem() 
            item['cancion'] = sel.xpath('p[contains(@class, "top-song")]/text()').extract();
            item['artista'] = sel.xpath('p[contains(@class, "top-autor")]/text()').extract();
            item['disco'] = sel.xpath('p[contains(@class, "top-disco")]/text()').extract();
            yield item 
