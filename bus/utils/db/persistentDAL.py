# -*- coding: utf-8 -*-

import pymysql

#TODO 持久化数据


import pymysql.cursors
import pymysql

class persistentUtils():


    def insertBusInfo(self,connection):
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `bus_name` FROM `bus_info` WHERE 1=1"
                cursor.execute(sql)
                result = cursor.fetchone()
                print(result)
        finally:
            self.connection.close()

