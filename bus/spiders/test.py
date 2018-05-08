# -*- coding: UTF-8 -*-
import requests
import bus.spiders.config as R
from lxml import etree
import lxml
import re

uri = R.uri_line_name

bus_info = {'lineid':'10335'}

#TODO 添加头
# res = requests.get(uri,params=bus_info)
# print(res.content.decode("utf-8"))
# data = res.content


data = '<lineInfoDetails>	<lineResults0>		<direction>true</direction>		<stop>			<zdmc>海阳路长清路</zdmc>			<id>687A0001</id>		</stop>		<stop>			<zdmc>海阳路灵岩南路</zdmc>			<id>687B0003</id>		</stop>		<stop>			<zdmc>海阳路上南路</zdmc>			<id>687C0003</id>		</stop>		<stop>			<zdmc>上南路杨思路</zdmc>			<id>6A7B0000</id>		</stop>		<stop>			<zdmc>上南路德州路</zdmc>			<id>6B7B0002</id>		</stop>		<stop>			<zdmc>成山路洪山路</zdmc>			<id>30469</id>		</stop>		<stop>			<zdmc>成山路云台路</zdmc>			<id>6C7D0003</id>		</stop>		<stop>			<zdmc>成山路东明路</zdmc>			<id>6C7E0004</id>		</stop>		<stop>			<zdmc>成山路邹平路</zdmc>			<id>6C7F0002</id>		</stop>		<stop>			<zdmc>杨高南路浦三路</zdmc>			<id>6E800003</id>		</stop>		<stop>			<zdmc>杨高南路高科西路</zdmc>			<id>70810000</id>		</stop>		<stop>			<zdmc>杨高南路严杨路</zdmc>			<id>71810000</id>		</stop>		<stop>			<zdmc>陆家浜路跨龙路</zdmc>			<id>757B0002</id>		</stop>		<stop>			<zdmc>陆家浜路大兴街</zdmc>			<id>757A0005</id>		</stop>		<stop>			<zdmc>老西门(西藏南路)</zdmc>			<id>76790006</id>		</stop>		<stop>			<zdmc>西藏南路淮海东路</zdmc>			<id>78780004</id>		</stop>		<stop>			<zdmc>金陵中路龙门路</zdmc>			<id>7878000A</id>		</stop>		<stop>			<zdmc>普安路延安东路</zdmc>			<id>78770003</id>		</stop>	</lineResults0>	<lineResults1>		<direction>false</direction>		<stop>			<zdmc>普安路延安东路</zdmc>			<id>78770003</id>		</stop>		<stop>			<zdmc>西藏南路宁海东路</zdmc>			<id>78780007</id>		</stop>		<stop>			<zdmc>西藏南路淮海东路</zdmc>			<id>78780002</id>		</stop>		<stop>			<zdmc>老西门（西藏南路）</zdmc>			<id>29643</id>		</stop>		<stop>			<zdmc>西藏南路陆家浜路</zdmc>			<id>75790001</id>		</stop>		<stop>			<zdmc>陆家浜路大兴街</zdmc>			<id>757A0004</id>		</stop>		<stop>			<zdmc>陆家浜路跨龙路</zdmc>			<id>757B0003</id>		</stop>		<stop>			<zdmc>杨高南路严杨路</zdmc>			<id>71810001</id>		</stop>		<stop>			<zdmc>杨高南路高科西路</zdmc>			<id>70810001</id>		</stop>		<stop>			<zdmc>杨高南路浦三路</zdmc>			<id>6E800005</id>		</stop>		<stop>			<zdmc>成山路邹平路</zdmc>			<id>6C7F0000</id>		</stop>		<stop>			<zdmc>成山路东明路</zdmc>			<id>6C7E0003</id>		</stop>		<stop>			<zdmc>成山路云台路</zdmc>			<id>6C7D0000</id>		</stop>		<stop>			<zdmc>成山路洪山路</zdmc>			<id>6C7C0002</id>		</stop>		<stop>			<zdmc>上南路德州路</zdmc>			<id>6B7B0004</id>		</stop>		<stop>			<zdmc>上南路杨思路</zdmc>			<id>6A7B0001</id>		</stop>		<stop>			<zdmc>海阳路上南路</zdmc>			<id>687C0001</id>		</stop>		<stop>			<zdmc>海阳路灵岩南路</zdmc>			<id>687B0002</id>		</stop>		<stop>			<zdmc>海阳路长清路</zdmc>			<id>687A0001</id>		</stop>	</lineResults1></lineInfoDetails>'

parser = etree.XMLParser()


parse_data = etree.XML(data, parser)
# parse_data = etree.HTML(data, parser)

#查找线路名称:
lineResultSet = set()
for i in re.findall("lineResults\d",data):
    lineResultSet.add(i)

#查找各个线路的站点名称跟id
for lineResult in lineResultSet:
    print(str(lineResult))
    all_stop = parse_data.xpath('//lineInfoDetails/'+str(lineResult)+'/stop')
    # print(all_stop)
    for stop in all_stop:
        print("id is: {0} , stop name is {1}".format(stop.find('id').text, stop.find('zdmc').text))
