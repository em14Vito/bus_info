# -*- coding: UTF-8 -*-
import requests

uri = 'http://180.166.5.82:8000/palmbus_serv/PalmBusJgj/getLineInfoByName.do'#?linename=583%E8%B7%AF"

bus_info = {'linename':'583路'}

#TODO 添加头
res = requests.get(uri,params=bus_info)
print(res.content.decode("utf-8"))

