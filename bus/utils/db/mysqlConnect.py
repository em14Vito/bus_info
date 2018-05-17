# -*- coding: UTF-8 -*-
import pymysql.cursors
import pymysql
import time
import datetime

# https://pypi.org/project/PyMySQL/


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
