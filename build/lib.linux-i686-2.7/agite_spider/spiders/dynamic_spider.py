# -*- coding: utf-8 -*-
import scrapy
from scrapy_rss import RssItem
class DynamicSpiderSpider(scrapy.Spider):
	name = 'dynamic_spider'
	start_urls = ['http://brewdog.com/browse/c-BrewdogBeer-1/']
	
	   

	def parse(self, response):

		for product in self.parse_products(response):
			yield product
		
		next_page = response.xpath(
			'//ul[@class="pagination"]/li[@class="next"]/a/@href'
		).extract_first()
		if next_page:
			url = response.urljoin(next_page)
			request = scrapy.Request(url)
			yield request
	
	def parse_products(self, response):
		items = response.xpath('//ul[contains(@class, "itemsList")]/li')
		for item in items:
			product = RssItem()
			title = item.xpath('.//h3/a/text()').extract_first().strip()
			url = item.xpath('.//h3/a/@href').extract_first()
			product_id = item.xpath('.//input[@name="id"]/@value').extract_first()
			price = item.xpath('.//span[@class="currencyPrice"]/text()').extract_first()
			product.title = title
			product.link = url
			product.description = price
			yield product    
