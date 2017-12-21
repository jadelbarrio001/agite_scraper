import scrapy
from scrapy_rss import RssItem

class SomeSpider(scrapy.Spider):
    name = 'first_spider'
    start_urls = ['http://www.diariovasco.com', 'http://www.noticiasdegipuzkoa.com', 'http://www.marca.com']
        

    def parse(self, response):

        for titulo in response.xpath('.//div'):
            item = RssItem()
            item.title = titulo.xpath('.//a/text()').extract_first()
            item.link = titulo.xpath('.//a/@href').extract_first()
            yield item
        

        
        
