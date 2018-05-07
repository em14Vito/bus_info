import pymysql.cursors
# https://pypi.org/project/PyMySQL/
import pymysql

class baseDB():

    connection = object

    def __init__(self):
        # Connect to the database
        self.connection = pymysql.connect(host='127.0.0.1',
                                     user='root',
                                     password='root',
                                     db='pika',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

    def test(self):
        try:

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            # connection.commit()

            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `bus_name` FROM `bus_info` WHERE 1=1"
                cursor.execute(sql)
                result = cursor.fetchone()
                print(result)
        finally:
            self.connection.close()


test = baseDB()
test.test()