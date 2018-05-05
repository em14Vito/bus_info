import scrapy

class QuotesSpider(scrapy.Spider):
    name = "sh_bus"
    ip = "180.166.5.82:8000"
    def start_requests(self):
        uri = "/palmbus_serv/PalmBusJgj/getLineInfoByName.do?linename=583%E8%B7%AF"
        yield scrapy.Request(url=ip+uri, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'bus-%s.xml' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)