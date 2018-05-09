# -*- coding: UTF-8 -*-
import pymysql.cursors
# https://pypi.org/project/PyMySQL/
import pymysql
import time
import datetime

class baseDB():

    connection = object

    def __init__(self):
        # Connect to the database
        self.connection = pymysql.connect(host='127.0.0.1',
                                     user='root',
                                     password='root',
                                     db='pika',
                                     # db='inscore_test',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)


    # def test(self):
    #     try:
    #
    #         # connection is not autocommit by default. So you must commit to save
    #         # your changes.
    #         # connection.commit()
    #
    #         cursor = self.connection.cursor()
    #
    #         ts = time.time()
    #         timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    #         sql = "INSERT INTO `bus_info` (`create_time`,`modify_time`,`bus_id`, `bus_name`) VALUES (%s,%s,%s,%s)"
    #         cursor.execute(sql,(timestamp,timestamp,'11','583路'))
    #         self.connection.commit()
    #     except BaseException as err:  # as 加原因参数名称
    #         print('Exception: ', err)
    #         self.connection.rollback()
    #     finally:
    #         self.connection.close()

