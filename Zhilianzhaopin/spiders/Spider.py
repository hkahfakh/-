# -*- coding: utf-8 -*-

import scrapy
from Zhilianzhaopin.items import ZhilianzhaopinItem
import json
     #设置name
class MSpider(scrapy.Spider):
    name = "MySpider"
    #设定域名
    allowed_domains = ["sou.zhaopin.com"]
    #填写爬取地址
    start_urls = ["http://sou.zhaopin.com/jobs/searchresult.ashx?jl=544&bj=160000&sj=045&sg=e749ffdf17d7456491ea6103f078f5f8&p=1"]
    #编写爬取方法rtr
    def parse(self, response):

        with open('data.json', 'wb') as f:
            f.write(response.body)

        item = ZhilianzhaopinItem()
        for box in response.xpath('//table'):
            #获取工作名称
            item['name'] = box.xpath('.//td/div/a/text()').extract_first()
            item['Company'] = box.xpath('.//td[3]/a[1]/text()').extract_first()
            item['Salary'] = box.xpath('.//td[@class="zwyx"]/text()').extract_first()
            item['location'] = box.xpath('.//td[5]/text()').extract_first()
            yield item

        next_page = response.xpath('//div[@class="pagesDown"]/ul/li[11]/a/@href').extract()[0]
        #print(next_page)    #查看xpath选取是否正确的好方法
        #print(type(next_page))
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse, headers={'referer': next_page})


