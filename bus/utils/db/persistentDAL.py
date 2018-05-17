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
        #持久化数据
        id = ''
        try:
            with self.connection.cursor() as cursor:
                cursor = self.connection.cursor()
                ts = time.time()
                timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                sql = "INSERT INTO `stop_info` (`create_time`,`modify_time`,`line_info_id`, `stop_id`, `stop_name`)"\
                    "VALUES (%s,%s,%s,%s,%s)"
                cursor.execute(sql, (timestamp, timestamp,data.get("line_info_id"),data.get("stop_id"),data.get("stop_name")))
                id = cursor.lastrowid
                self.connection.commit()
        except BaseException as err:  # as 加原因参数名称
            # self.log('Exception: %s' % err,level=logging.ERROR)
            print('Exception: %s' % err)
            self.connection.rollback()
        # finally:
        #     self.connection.close()


    def insertRealTimeStopInfo(self,data):
        #持久化数据
        id = ''
        try:
            with self.connection.cursor() as cursor:
                cursor = self.connection.cursor()
                ts = time.time()
                timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                sql = "INSERT INTO `stop_real_time_msg` (`create_time`,`modify_time`,`stop_info_id`, `car_name`, `distance`," \
                      "`remain_time`,`remain_stop`)"\
                    "VALUES (%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, (timestamp, timestamp,data.get("stop_info_id"),data.get("car_name"),
                                     data.get("distance"),data.get("remain_time"),data.get("remain_stop")))
                id = cursor.lastrowid
                self.connection.commit()
        except BaseException as err:  # as 加原因参数名称
            print('Exception: %s' % err)
            self.connection.rollback()
