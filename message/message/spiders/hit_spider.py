#-*- coding: utf-8 -*-
import scrapy
from message.items import MessageItem

class hit_spider(scrapy.Spider):
    name = "hit_spider"
    allowed_domains = ["news.hitwh.edu.cn"]
    start_urls = [
        "http://news.hitwh.edu.cn/news_list.asp?id=1"
    ]
    def parse(self,response):
        #item = MessageItem()
        for i in range(1,4):
            item_url = "http://news.hitwh.edu.cn/news_list.asp?page=" + "i" + "&id=1&nid="
            yield scrapy.Request(item_url,callback=self.parse_url)
            #yield item
    def parse_url(self,response):
        item = MessageItem()
        for box in response.xpath('//li/a[@class = "size14"]'):
            item['title'] = box.xpath(".//text()").extract()[0].strip()
            url = "http://news.hitwh.edu.cn/"+ box.xpath(".//@href").extract()[0]
            item['url_next'] = url
            yield scrapy.Request(url,meta={'item':item},callback=self.parse_item)

    def parse_item(self,response):
        item = response.meta['item']
        text = " "
        for box in response.xpath('//span'):
            text = text+box.xpath('string(.)').extract()[0]
        item['text']=text
        yield item
