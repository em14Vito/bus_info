# -*- coding: UTF-8 -*-
import requests
import bus.spiders.config as R
from lxml import etree
uri = R.uri_bus_name

bus_info = {'linename':'782路'}

#TODO 添加头
res = requests.get(uri,params=bus_info)
print(res.content.decode("utf-8"))
data = res.content
# data = '''
#         <linedetail>
#             <end_earlytime>05:30</end_earlytime>
#             <end_latetime>22:30</end_latetime>
#             <end_stop>懿行路和炯路</end_stop>
#             <line_id>10225</line_id>
#             <line_name>583路</line_name>
#             <start_earlytime>05:30</start_earlytime>
#             <start_latetime>22:30</start_latetime>
#             <start_stop>陆家嘴</start_stop>
#         </linedetail>
#
#        '''

parse_data = etree.HTML(data)
end_last_time = parse_data.xpath('//linedetail/end_stop/text()')
print(end_last_time)

