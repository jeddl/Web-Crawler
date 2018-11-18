import scrapy
from webwithin.items import WebwithinItem

class WebWithin(scrapy.Spider):
    name = "webwithin"

    def start_requests(self):
        # Start Url
        nba_url = "https://www.nba.com/news"

        start_urls = []
        start_urls.append(nba_url)
        for url in start_urls:
            yield scrapy.Request(url = url, callback = self.parse)
    
    def parse(self, response):
        nbaItem = WebwithinItem()

        # TODO: Infinite Page Scrapying
        #response.xpath("//*[@id='block-collectionlistblock']/div").extract()
        nbaItem['nbaNewsTitle'] = ''
        nbaItem['nbaNewsContent'] = ''
        nbaNewsBody = "Body"

        filename = "NBA News.html"
        with open(filename, 'w') as f:
            f.write(nbaNewsBody)


    def getNbaNewsBody(self, newsTitle, newsContent):
        return newsTitle + "\n" + newsContent
