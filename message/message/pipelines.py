# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import json
import codecs
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class MessagePipeline(object):
    def process_item(self, item, spider):
        return item

class hit_spiderPipline(object):
    def __init__(self):
        #入库
        #try:  
           # self.db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="lin952787655", port=3306, db="message",  charset="utf8")  
            #self.cursor = self.db.cursor()
            #self.cursor.execute("DROP TABLE IF EXITS textdata")
            #print "Connect to db successfully!"  

        #except:  
            #print "Fail to connect to db!" 
        #文件
        self.file = codecs.open('new_message.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        #入库
        #文件
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.db.commit() 
        self.db.close 
        self.file.close()

from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

class MySQLStorePipeline(object):

    def __init__(self):
        dbargs = dict(
             host = '127.0.0.1',
             db = 'message',
             user = 'root',
             passwd = 'lin952787655',
             #cursorclass = MySQLdb.cursors.DictCursor,
             charset = 'utf8',
             use_unicode = True
            )
        self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)
        

    def process_item(self, item,spider):
        res = self.dbpool.runInteraction(self.insert_into_table,item)
        return item


    def insert_into_table(self,conn,item):
        #print item['title']
        #print item['url_next']
        #print item['text']
        conn.execute('insert into textdata(title, url, text) values(%s,%s,%s)', ("http"," http://sdfa","ni"))

