# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from items import qidianBookListTtem
from scrapy_redis.spiders import RedisSpider



class QidianspiderSpider(RedisSpider):
    name = 'qidianSpider'
    allowed_domains = ['https://www.qidian.com']
    redis_key = "qidianspider:star_urls"
    start_urls = ['https://www.qidian.com/all']

    def parse(self, response):
        books = response.xpath('//li[@data-rid]')
        next_url  = response.css('.lbf-pagination-next ::attr(href)').extract()
        for book in books:
            novelImageUrl = book.css('.book-img-box a img::attr(src)').extract()
            novelId = book.css('.book-img-box a::attr(data-bid)').extract()
            novelDetailUrl = book.xpath('.//div[@class="book-mid-info"]/h4/a/attribute::href').extract()
            novelName = book.xpath('.//div[@class="book-mid-info"]/h4/a/text()').extract()
            novelAllList = book.xpath('.//p[@class="author"]/a/text()').extract()
            novelDoing = book.xpath('.//p[@class="author"]/span/text()').extract()

            qidianBookList = qidianBookListTtem()
            qidianBookList['novelId'] = novelId
            qidianBookList['novelDetailUrl'] = novelDetailUrl
            qidianBookList['novelName'] = novelName
            qidianBookList['novelAllList'] = novelAllList
            qidianBookList['novelProcess'] = novelDoing
            qidianBookList['novelImageUrl'] = novelImageUrl

            yield qidianBookList
        yield scrapy.Request('https:'+next_url[0],callback=self.parse)





