import scrapy
from webwithin.items import Fundrazr

class WebWithinFundrazr(scrapy.Spider):
    name = "fundrazr"

    # Start URL
    start_urls = ["https://fundrazr.com/find?category=Health"]

    # Crawl info from page 1 to 8
    for i in range(2, 8):
        start_urls.append("https://fundrazr.com/find?category=Health&page="+str(i)+"")
	
    def parse(self, response):
    	for href in response.xpath("//h2[contains(@class, 'title headline-font')]/a[contains(@class, 'campaign-link')]//@href"):
    		url  = "https:" + href.extract() 
    		yield scrapy.Request(url, callback=self.parseContent)

    def parseContent(self, response):
        item = Fundrazr()
        item['title'] = response.xpath("//div[contains(@id, 'campaign-title')]/descendant::text()").extract()[0].strip()
        item['currentAmount']= response.xpath("//span[contains(@class, 'stat')]/span[contains(@class, 'amount-raised')]/descendant::text()").extract()
        item['goal'] = " ".join(response.xpath("//div[contains(@class, 'stats-primary with-goal')]//span[contains(@class, 'stats-label hidden-phone')]/text()").extract()).strip()
        item['currencyType'] = response.xpath("//div[contains(@class, 'stats-primary with-goal')]/@title").extract()
        item['endDate'] = "".join(response.xpath("//div[contains(@id, 'campaign-stats')]//span[contains(@class,'stats-label hidden-phone')]/span[@class='nowrap']/text()").extract()).strip()
        item['contributors'] = response.xpath("//div[contains(@class, 'stats-secondary with-goal')]//span[contains(@class, 'donation-count stat')]/text()").extract()
        story_list = response.xpath("//div[contains(@id, 'full-story')]/descendant::text()").extract()
        story_list = [x.strip() for x in story_list if len(x.strip()) > 0]
        item['story']  = " ".join(story_list)
        item['url'] = response.xpath("//meta[@property='og:url']/@content").extract()
        yield item








