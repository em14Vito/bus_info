# -*- coding: UTF-8 -*-
import scrapy
import requests
import bus.spiders.config as R
from lxml import etree
import logging
from urllib import parse
from bus.utils.db.persistentDAL import persistentUtils
from bus.utils.db.accessDBDAL import accessUtils
import re


class RealTimeSpider(scrapy.Spider):

    name = 'real_time_stop_info'
    persistent = object
    access = object
    allowed_domains = ["bsth.tech"]

    # 初始化操作
    def defined_init(self):
        self.persistent = persistentUtils()
        self.access = accessUtils()
    # 初始爬取 bus_info
    def start_requests(self):
        self.defined_init()

        self.log("Start Crawl by Real Time Info",level=logging.INFO)

        favour_info = self.access.selectFavourBusStopInfo()

        for item in favour_info:
            params = {'lineid': item.get('bus_id'),
                      'stopid': item.get('stop_id'),
                      'direction': item.get('direction_id')
                      }
            yield scrapy.Request(url=R.uri_stop_real_time_monitor+"?"+parse.urlencode(params),
                                 callback=self.deal_real_time_info,method='GET',meta={'favour':favour_info})



    # 处理bus 基本 的信息(持久化)
    def deal_real_time_info(self,response):
        resp = response.body.decode("utf-8")
        print(resp)



