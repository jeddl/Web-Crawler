import scrapy
from webwithin.items import CnnNews

class WebWithin(scrapy.Spider):
    name = "cnn_news"
    
    # Start Url
    cnn_url_base = "https://www.cnn.com/"
    cnn_url_us = cnn_url_base + "us"

    start_urls = []
    start_urls.append(cnn_url_us)

    def parse(self, response):
        for href in response.xpath("//*[@id='us-zone-1']/div[2]/div/div[1]/ul/li/article/div/div/h3//@href"):
            url = "https://www.cnn.com" + href.extract()
            yield scrapy.Request(url = url, callback = self.parseContent)
    
    def parseContent(self, response):
        item = CnnNews()
        item['title'] = response.xpath("/html/body/div[contains(@class, 'pg-wrapper')]/article/div[contains(@class, 'l-container')]/h1/text()").extract()
        content_sum = response.xpath("//*[@id='body-text']/div[contains(@class, 'l-container')]/div/p/text()").extract()
        content_1 = response.xpath("//*[@id='body-text']/div[contains(@class, 'l-container')]/div/text()").extract()
        content_2 = response.xpath("//*[@id='body-text']/div[contains(@class, 'l-container')]/div/div/text()").extract()
        item['content'] = content_sum + content_1 + content_2
        yield item