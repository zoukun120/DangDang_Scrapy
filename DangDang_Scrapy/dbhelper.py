import pymysql
from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings  # 导入seetings配置
import time

#  读取settings中的配置
class DBHelper:

    def __init__(self):
        settings = get_project_settings()  # 获取settings配置，设置需要的信息
        dbparams = dict(
            host=settings['MYSQL_HOST'],  # 读取settings中的配置
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)   # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        self.dbpool = dbpool


    # 写入数据库中
    # 参数xxx随便命名，都能调用execute
    def insert_to_db(self,xxx,item):
        sql_insert = 'insert into dangdang(time,name,author,price_n,price_s,discount,comment_num,detail,rank,publish_time ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        params = (
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
            item['book_name'],
            item['author'],
            item['price_n'],
            item['price_s'],
            item['discount'],
            item['comment_num'],
            item['detail'],
            item['rank'],
            item['release']
        )
        xxx.execute(sql_insert, params)

