# -*- coding: utf-8 -*-
import scrapy
#from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.http.response.html import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy import signals
from scrapy import exceptions

class TutorialSpider(scrapy.Spider):
    name = 'tutorial'
    # allowed_domains = ["theculturetrip.com"]
    # offset = 0
    # scrolled_article = []
    # header = {
    #     'Accept': 'application/json',
    #     'Content-Type': 'application/json',
    #     'Origin': 'https://theculturetrip.com',
    #     'Referer': 'https://theculturetrip.com/asia/malaysia/',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    # }

    def __init__(self, *args, **kwargs):
        super(TutorialSpider, self).__init__(*args, **kwargs)
        self.le = LinkExtractor()

    def parse(self, response):
        if not isinstance(response, HtmlResponse):
            return

        for link in self.le.extract_links(response):
            r = Request(url=link.url)
            r.meta.update(link_text=link.text)
        # print(response.text)
        # print('debug')
        # self.offset = self.offset + 15
        # next_url = response.urljoin('https://app.theculturetrip.com/cultureTrip-api/v2/articles?kgID=13211594601088724956&queryType=location_page&offset='+str(self.offset)+'&limit=15')
        # r = Request(url=next_url)
        # r.headers.update(self.header)
        # r.headers = self.header
            yield r

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = cls(*args, **kwargs)
        spider._set_crawler(crawler)
        spider.crawler.signals.connect(
            spider.spider_idle, signal=signals.spider_idle)
        return spider

    def spider_idle(self):
        self.log("Spider idle signal caught.")
        raise exceptions.DontCloseSpider
