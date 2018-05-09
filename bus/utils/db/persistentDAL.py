# -*- coding: utf-8 -*-

import pymysql
import time
import datetime
from bus.utils.db.mysqlConnect import baseDB
import logging
#TODO 持久化数据


import pymysql.cursors
import pymysql

class persistentUtils(baseDB):

    #插入数据到 busInfo 表
    def insertBusInfo(self, data):
        id = ''
        try:
            with self.connection.cursor() as cursor:
                cursor = self.connection.cursor()
                ts = time.time()
                timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                sql = "INSERT INTO `bus_info` (`create_time`,`modify_time`,`bus_id`, `bus_name`) VALUES (%s,%s,%s,%s)"
                cursor.execute(sql, (timestamp, timestamp,data.get("bus_id"),data.get("bus_name")))
                id = cursor.lastrowid
                self.connection.commit()
        except BaseException as err:  # as 加原因参数名称
            # self.log('Exception: %s' % err,level=logging.ERROR)
            print('Exception: %s' % err)
            self.connection.rollback()
        # finally:
        #     self.connection.close()
        return id

    def insertLineInfo(self,data):
        id = ''
        try:
            with self.connection.cursor() as cursor:
                cursor = self.connection.cursor()
                ts = time.time()
                timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                sql = "INSERT INTO `line_info` " \
                      "(`create_time`,`modify_time`,`bus_info_id`, `direction_id`,`direction_start_stop`,`direction_end_stop`,`earliest_departure_time`,`lastest_departure_time`)" \
                      " VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, (timestamp, timestamp,data.get("bus_info_id"),data.get("direction_id"),data.get("direction_start_stop"),
                                     data.get("direction_end_stop"),data.get("earliest_departure_time"),data.get("lastest_departure_time")))
                id = cursor.lastrowid
                self.connection.commit()
        except BaseException as err:  # as 加原因参数名称
            # self.log('Exception: %s' % err,level=logging.ERROR)
            print('Exception: %s' % err)
            self.connection.rollback()
        # finally:
        #     self.connection.close()
        return id

    def insertStopInfo(self,data):
        #TODO 持久化数据
        return ''