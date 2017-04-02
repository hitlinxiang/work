# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import json
import codecs
from os import path
from scrapy.xlib.pydispatch import dispatcher

class ScrapytextPipeline(object):
    def process_item(self, item, spider):
        return item

class MyPipeline(object):
    def __init__(self):
        #入库
        #文件
        self.file = codecs.open('cnblogs.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        #入库
        #文件
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()

class MytextDataPipeline(object):
    def from_settings(cls,settings)

