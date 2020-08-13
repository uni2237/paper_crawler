import scrapy
from urllib.parse import urlencode


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
        url += urlencode(params)
        yield scrapy.Request(url=url)


def parse(self, response):
    print(response.body)

# 출처: https://engkimbs.tistory.com/962?category=807933 [새로비]
