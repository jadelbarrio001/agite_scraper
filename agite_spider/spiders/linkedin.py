# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy_rss import RssItem

class LinkedinSpider(scrapy.Spider):
    name = 'linkedin'
    allowed_domains = ['linkedin.com']
    login_url = 'https://www.linkedin.com/uas/login'
    start_urls = ['https://www.linkedin.com/company/10296761/']

    def parse(self, response):
        csrf_token = response.css('input[name="loginCsrfParam"]::attr(value)').extract_first()
    	data = {
    		
    		'session_key' : 'si10.jadelbarrio001@gmail.com',
    		'session_password' : '2lehaqa3!'
    	}
    	yield FormRequest(url = self.login_url, formdata = data, callback = self.parse_products)

    def parse_products(self, response):
		items = response.xpath('.//*')
		for item in items:
			product = RssItem()
			title = 'prueba linkedin'
			url = item.xpath('.//a/@href').extract_first()
			
			product.title = title
			product.link = url
			
			yield product  