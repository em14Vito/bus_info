# -*- coding: UTF-8 -*-
import scrapy
import requests
import bus.spiders.config as R
from lxml import etree
import logging
from urllib import parse
from bus.utils.db.persistentDAL import persistentUtils
import re


class QuotesSpider(scrapy.Spider):

    record_bus_name = ["583路", "782路"]
    name = 'base_bus_info'
    persistent = object
    allowed_domains = ["bsth.tech"]


    def defined_init(self):
        self.persistent = persistentUtils()

    # 初始爬取 bus_info
    def start_requests(self):
        self.defined_init()

        self.log("Start scrapy bus",level=logging.INFO)
        for item in self.record_bus_name:
            params = {'linename': item}
            yield scrapy.Request(url=R.uri_bus_name+"?"+parse.urlencode(params),
                                 callback=self.parse_lineInfo,method='GET')



    # 继续爬取 line_info 的信息
    def parse_lineInfo(self,response):

        resp = response.body.decode("utf-8")
        self.log("公交信息请求结果%s"%resp,level=logging.INFO)

        params = {'lineid': ''}
        try:
            bus_info_data = self.deal_bus_info(response.body)
            params['lineid'] = bus_info_data.get('bus_id')
        except BaseException as err:  # as 加原因参数名称
            self.log('Exception: %s' % err, level=logging.ERROR)

        yield scrapy.Request(url=R.uri_line_name+"?"+parse.urlencode(params),
                             callback=self.deal_line_and_stop_info,method='GET',
                             meta={'bus_info':bus_info_data})


    # 处理bus 基本 的信息(持久化)
    def deal_bus_info(self,data):
        #解析整个报文并提取数据成key-value 形式
        parser = etree.XMLParser()
        parse_data = etree.HTML(data, parser)
        bus_id = parse_data.xpath('//linedetail/line_id/text()')[0]
        bus_name = parse_data.xpath('//linedetail/line_name/text()')[0]
        end_earlytime = parse_data.xpath('//linedetail/end_earlytime/text()')[0]
        end_latetime = parse_data.xpath('//linedetail/end_latetime/text()')[0]
        end_stop = parse_data.xpath('//linedetail/end_stop/text()')[0]
        start_earlytime = parse_data.xpath('//linedetail/start_earlytime/text()')[0]
        start_latetime = parse_data.xpath('//linedetail/start_latetime/text()')[0]
        start_stop = parse_data.xpath('//linedetail/start_stop/text()')[0]

        do = {'bus_id': bus_id, 'bus_name': bus_name}
        # 持久化数据，获得对应的id
        id = self.persistent.insertBusInfo(do)

        result = {'bus_info_id':id,
                  'bus_id': bus_id,
                  'bus_name': bus_name,
                  'end_earlytime': end_earlytime,
                  'end_latetime': end_latetime,
                  'end_stop': end_stop,
                  'start_earlytime': start_earlytime,
                  'start_latetime': start_latetime,
                  'start_stop': start_stop}
        return result

    # 处理站点(线路)信息 (持久化)
    def deal_line_and_stop_info(self,response):

        #处理 线路概要信息
        bus_info_data = response.meta['bus_info']
        line_info = self.deal_line_info(bus_info_data)


        #处理 站点信息
        data = response.body
        parser = etree.XMLParser()
        parse_data = etree.HTML(data, parser)

        #查找线路名称:
        lineResultSet = set()
        try:
            for i in re.findall("lineResults\d",data.decode('utf-8')):
                lineResultSet.add(i)
        except BaseException as err:
            print('Exception: %s' % err)

        #查找各个线路的站点名称跟id
        for lineResult in lineResultSet:

            all_stop = parse_data.xpath('//lineInfoDetails/'+str(lineResult)+'/stop')
            #TODO 根据第一个stop的name，找出对应的line_info_id (从 dict (line_info ) 中)
            # print(all_stop)
            for stop in all_stop:
                #TODO 持久化对应的站点信息
                print("id is: {0} , stop name is {1}".format(stop.find('id').text, stop.find('zdmc').text))


    def deal_line_info(self,data):
        #正向:
        positive_way = {
            'bus_info_id':data.get('bus_info_id'),
            'direction_id':'0',
            'direction_start_stop':data.get('start_stop'),
            'direction_end_stop':data.get('end_stop'),
            'earliest_departure_time':data.get('start_earlytime'),
            'lastest_departure_time': data.get('start_latetime')
        }

        #反向:  negative
        negative_way = {
            'bus_info_id':data.get('bus_info_id'),
            'direction_id':'1',
            'direction_start_stop':data.get('end_stop'),
            'direction_end_stop':data.get('start_stop'),
            'earliest_departure_time':data.get('end_earlytime'),
            'lastest_departure_time': data.get('end_latetime')
        }

        result = {}
        # 持久化数据，获得对应的id
        id = self.persistent.insertLineInfo(positive_way)
        result[positive_way.get('direction_start_stop')] = id

        id = self.persistent.insertLineInfo(negative_way)
        result[negative_way.get('direction_start_stop')] = id

        return result