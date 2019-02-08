import copy
from DangDang_Scrapy.dbhelper import DBHelper


class DangdangScrapyPipeline(object):

    # 连接数据库
    def __init__(self):
        self.db = DBHelper()

    # 对 item 字段进行处理
    def process_item(self, item, spider):
        item['rank'] = item['rank'][:item['rank'].index('.')]
        item['comment_num'] = item['comment_num'][:item['comment_num'].index('条')]
        item['price_n'] = item['price_n'][item['price_n'].index('¥')+1:]
        item['price_s'] = item['price_s'][:item['price_s'].index('折')]
        item['discount'] = item['discount'][:item['discount'].index('折')]
        asynItem = copy.deepcopy(item)
        self.db.dbpool.runInteraction(self.db.insert_to_db, asynItem)
        return item



