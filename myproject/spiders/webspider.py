# -*- coding: utf-8 -*-
import scrapy
from myproject.items import MyprojectItem
import re
import datetime
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class WebspiderSpider(scrapy.Spider):
    name = 'webspider'
    allowed_domains = ['www.wai-gaya.site']
    start_urls = ['https://www.wai-gaya.site/']

    xpath = {
        'title' : "//title/text()",
    }
 
    rules = (
        Rule(LinkExtractor(
            allow=('index\.php', ), 
            deny=('wp-login\.php', ) 
            ),
            callback='parse_item'
        ),
    )

    # データ抽出関数定義
    def parse(self, response): # response に、ウェブサイトの情報が入っている
        item = MyprojectItem() # items.pyで指定したクラス
        item['title'] = response.xpath(self.xpath['title']).extract()[0]
        item['link'] = response.url
        item['date'] = datetime.datetime.utcnow() + datetime.timedelta(hours=9) # 現在時間。日本時間にして突っ込む。

        yield item
