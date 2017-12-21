# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy_rss import RssItem

class ResearchgateSpider(scrapy.Spider):
    name = 'researchgate'
    allowed_domains = ['researchgate.net']
    login_url = 'http://researchgate.net/login'
    start_urls = ['https://www.researchgate.net/home']

    def parse(self, response):
    	csrf_token = response.css('input[name="request_token"]::attr(value)').extract_first()
    	data = {
    		'request_token' : csrf_token,
    		'login' : 'jprado@lortek.es',
    		'password' : 'I12345l'
    	}
    	yield FormRequest(url=self.login_url, formdata=data, callback=self.parse_products)
    
    def parse_products(self, response):
		items = response.xpath('.//div')
		for item in items:
			product = RssItem()
			title = 'prueba researchgate'
			url = item.xpath('.//a/@href').extract_first()
			
			product.title = title
			product.link = url
			
			yield product   
