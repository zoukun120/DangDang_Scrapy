import scrapy
from scrapy import Selector

from DangDang_Scrapy.items import DangdangScrapyItem

class spider(scrapy.Spider):
    name = 'book'
    url =  'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-'
    start_urls = []
    for index in range(1,11,1):
        start_urls.append(url+str(index))

    def parse(self, response):
        item = DangdangScrapyItem()
        ul = response.css('.bang_list li')
        # 去掉 \r\n 符号 .replace('\r','').replace('\n','')
        for li in ul:
            item['rank'] = li.css('.list_num::text').extract_first()
            item['detail'] = li.css('.pic a::attr(href)').extract_first()
            item['book_name'] = li.css('.name a::attr(title)').extract_first()
            item['comment_num'] = li.css('.star a::text').extract_first()
            item['author'] = li.css('.publisher_info a::text').extract_first()
            item['release'] = li.css('.publisher_info span::text').extract_first()
            item['price_n'] = li.css('.price_n::text').extract_first()
            item['price_s'] = li.css('.price_s::text').extract_first()
            item['discount'] = li.css('.price_s::text').extract_first()
            yield item





