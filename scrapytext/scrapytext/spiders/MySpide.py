#-*- coding: utf-8 -*-
import scrapy
from scrapytext.items import ScrapytextItem

class MySpider(scrapy.Spider):
    name = "MySpider"
    allowed_domains = ["imooc.com"]
    start_urls = [
        "http://www.imooc.com/course/list?page=1"
    ]
    def parse(self, response):
        item = ScrapytextItem()
        for box in response.xpath('//div[@class="index-card-container course-card-container container "]'):
            item['title'] = box.xpath('.//h3/text()').extract()[0].strip()
            item['image_url'] = box.xpath('.//@src').extract()[0]
            #item['student'] = box.xpath('.//span/text()').extract()[0].strip()
            item['introduction'] = box.xpath('.//p/@title').extract()[0].strip()
            url_next= 'http://www.imooc.com' + box.xpath('.//@href').extract()[0]
            item['url'] = url_next
            yield item
            yield scrapy.Request(url_next,callback=self.parse_item)
    def parse_item(self,response):
        print 999
