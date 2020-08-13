import scrapy
from scrapy import Selector

from paper_crawler.paper_crawler.items import PaperCrawlerItem

import time


class TradeSpider(scrapy.spiders.XMLFeedSpider):
    name = 'acl'


def start_requests(self):
    association = "acl"
    urls = [
        "https://www.aclweb.org/anthology/events/acl-2020/",
        "https://www.aclweb.org/anthology/events/acl-2019/",
        "https://www.aclweb.org/anthology/events/acl-2018/"
    ]
    params = {
        # 교수님께서 row를 1씩 받아오는 게 편하다고 말씀하셨던 걸로 기억해서 numOfRows를 1로 설정
        "numOfRows": "1",
    }
    for url in urls:
        yield scrapy.Request(url, self.parse)


def parse(self, response):
    for sel in response.xpath(''):
        item = PaperCrawlerItem()

        item['title'] = sel.xpath('//*[@id="p19-1"]/p[2]/span[2]/strong/a/text()').extract()[0]
        item['author'] = sel.xpath('/html/body/div/section/div[2]/p[2]/span[2]/a[1]/text()').extract()[0]
        item['abstraction'] = sel.xpath('//*[@id="abstract-P19-1001"]/div/text()').extract()[0]

        print('*' * 100)
        print(item['title'])

        time.sleep(5)

        yield item

# 출처: https://engkimbs.tistory.com/962?category=807933 [새로비]
