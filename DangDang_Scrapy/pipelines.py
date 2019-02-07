# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangScrapyPipeline(object):
    # 对 item 字段进行处理
    def process_item(self, item, spider):
        item['rank'] = item['rank'][:item['rank'].index('.')]
        item['comment_num'] = item['comment_num'][:item['comment_num'].index('条')]
        item['price_n'] = item['price_n'][item['price_n'].index('¥'):]
        item['price_s'] = item['price_s'][:item['price_s'].index('折')]
        item['discount'] = item['discount'][:item['discount'].index('折')]
        return item
