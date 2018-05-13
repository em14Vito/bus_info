# -*- coding: utf-8 -*-

from scrapy import cmdline

import time, os
# name = 'base_bus_info'
name = 'real_time_stop_info'
cmd = 'scrapy crawl {0}'.format(name)

def re_exe(inc):
    while True:
        os.system(cmd)
        # cmdline.execute(cmd.split())
        time.sleep(inc)

while True:
    re_exe(10)