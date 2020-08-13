# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PaperCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # /html/body/div/section/div[2]/p[2]/span[2]/strong/a/text()
    # //*[@id="p19-1"]/p[2]/span[2]/strong/a/text()
    # 19년의 경우, id="p-19-54"까지 있음.
    title = scrapy.Field()

    # //*[@id="p19-k"]/p[1] 여기서 k는 임의의 수고, p[1]은 큰제목인 것 같음. /span[1]도 마찬가지니 크롤링 할 필요가 없다고 판단.

    # /html/body/div/section/div[2]/p[2]/span[2]/a[i]/text() -> 확실친 않음
    # /html/body/div/section/div[2]/p[2]/span[2]/a[1]원랜 처음게 이거였는데, 필요한 건 링크가 아니라 이름 자체의 String이므로 /text()로 도전
    # //*[@id="p19-1"]/p[2]/span[2]/a[i]
    authors = scrapy.Field()

    # /html/body/div/section/div[2]/div[1]/div/text()
    # //*[@id="abstract-P19-1001"]/div/text()
    abstraction = scrapy.Field()

    # 크롬 관리자 모드에서 보면 title + authors가 d_block으로 묶여 있다.
    # /html/body/div/section/div[2]/p[2]/span[2]
    # //*[@id="p19-1"]/p[2]/span[2]
    # d_block = scrapy.Field()
    pass
