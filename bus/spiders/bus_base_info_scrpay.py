import scrapy
import requests
import bus.spiders.config as R
from lxml import etree
import lxml
import re
import logging
from urllib import parse



class QuotesSpider(scrapy.Spider):

    record_bus_name = ["583路", "782路"]
    name = 'base_bus_info'

    allowed_domains = ["bsth.tech"]


    def start_requests(self):
        self.log("Start scrapy bus",level=logging.INFO)
        for item in self.record_bus_name:
            params = {'linename': item}
            yield scrapy.Request(url=R.uri_bus_name+"?"+parse.urlencode(params),  callback=self.parse_lineInfo,method='GET')




    def parse_lineInfo(self,response):

        resp = response.body.decode("utf-8")
        print(resp)
        self.log(resp,level=logging.INFO)
        self.deal_bus_info(resp)




    def deal_bus_info(self,data):
        parser = etree.XMLParser()
        parse_data = etree.HTML(data, parser)
        bus_id = parse_data.xpath('//linedetail/line_id/text()')
        bus_name = parse_data.xpath('//linedetail/line_name/text()')