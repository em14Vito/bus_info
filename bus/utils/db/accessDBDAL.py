# -*- coding: utf-8 -*-

import pymysql
from bus.utils.db.mysqlConnect import baseDB

#TODO 读取DB数据库信息

class accessUtils(baseDB):

    def selectBusInfoByBusName(self,bus_name):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM `bus_info` WHERE `bus_name`=%s"
            cursor.execute(sql, (bus_name))
            result = cursor.fetchall()
            return result

    def selectBusInfoById(self,id):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM `bus_info` WHERE `bus_info_id`=%s"
            cursor.execute(sql,(id))
            result = cursor.fetchall()
            return result

    # 选取感兴趣的bus_info
    def selectFavourBusStopInfo(self):
        with self.connection.cursor() as cursor:
            sql = """
                SELECT stop_info_id,bus_id,stop_id,direction_id,stop_name
                FROM stop_info main
                LEFT JOIN line_info line
                ON main.line_info_id = line.line_info_id
                LEFT JOIN bus_info bus
                ON line.bus_info_id = bus.bus_info_id
                WHERE is_favour = 1
            """
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


d = accessUtils()
result = d.selectBusInfoByBusName('583路')
result = d.selectFavourBusStopInfo()
print(result)

