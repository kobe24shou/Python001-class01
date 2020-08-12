# -*- coding: utf-8 -*-
import scrapy
from spiders.items  import SpidersItem  
from scrapy.selector import Selector
from bs4 import BeautifulSoup

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan_movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']
                  
    def parse(self,response):
        items = []
        i=0
        top=10
        for each in response.xpath('//div[@class="movie-hover-info"]'):
            if(i<top):
                item = SpidersItem()
                title = each.xpath('div[2]/@title').extract_first().strip()
                category = each.xpath('div[2]/text()[2]').extract_first().strip()
                date = each.xpath('div[4]/text()[2]').extract_first().strip()

                item['title'] = title 
                item['category'] = category 
                item['date'] = date 
                print('-------------------')
                items.append(item)
                i+=1
            else:
                break
            yield item