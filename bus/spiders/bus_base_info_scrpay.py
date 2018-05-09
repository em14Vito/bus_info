# -*- coding: UTF-8 -*-
import scrapy
import requests
import bus.spiders.config as R
from lxml import etree
import logging
from urllib import parse
from bus.utils.db.persistentDAL import persistentUtils



class QuotesSpider(scrapy.Spider):

    record_bus_name = ["583路", "782路"]
    name = 'base_bus_info'
    persistent = object
    allowed_domains = ["bsth.tech"]


    def defined_init(self):
        self.persistent = persistentUtils()


    def start_requests(self):
        self.defined_init()

        self.log("Start scrapy bus",level=logging.INFO)
        for item in self.record_bus_name:
            params = {'linename': item}
            yield scrapy.Request(url=R.uri_bus_name+"?"+parse.urlencode(params),
                                 callback=self.parse_lineInfo,method='GET')




    def parse_lineInfo(self,response):

        resp = response.body.decode("utf-8")
        self.log("请求结果%s"%resp,level=logging.INFO)
        try:
            self.deal_bus_info(response.body)
        except BaseException as err:  # as 加原因参数名称
            self.log('Exception: %s' % err, level=logging.ERROR)




    def deal_bus_info(self,data):
        parser = etree.XMLParser()
        parse_data = etree.HTML(data, parser)
        bus_id = parse_data.xpath('//linedetail/line_id/text()')
        bus_name = parse_data.xpath('//linedetail/line_name/text()')

        data = {'bus_id': bus_id, 'bus_name': bus_name}
        self.persistent.insertBusInfo(data)

