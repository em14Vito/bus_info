# -*- coding: utf-8 -*-

from scrapy import cmdline
# name = 'base_bus_info'
name = 'real_time_stop_info'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())