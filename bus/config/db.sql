# v1 start
# time : 2018年05月06日18:55:17
CREATE TABLE `stop_info` (
  `stop_info_id` int(16) unsigned NOT NULL AUTO_INCREMENT,
  `create_time` timestamp NULL DEFAULT NULL,
  `modify_time` timestamp NULL DEFAULT NULL,
  `line_info` int(16) DEFAULT NULL,
  `stop_id` varchar(30) DEFAULT NULL,
  `stop_name` int(11) DEFAULT NULL,
  `car_name` int(11) DEFAULT NULL,
  `distance` int(20) DEFAULT NULL COMMENT '车距离该站点距离多远 , 单位 米',
  `remain_time` int(20) DEFAULT NULL COMMENT '大约还剩下多少时间,单位 秒',
  `remain_stop` int(20) DEFAULT NULL COMMENT '大约还剩下多少个站点, ',
  PRIMARY KEY (`stop_info_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `line_info` (
  `line_info_id` int(16) unsigned NOT NULL AUTO_INCREMENT,
  `create_time` timestamp NULL DEFAULT NULL,
  `modify_time` timestamp NULL DEFAULT NULL,
  `bus_info_id` int(16) DEFAULT NULL COMMENT '外键关联bus',
  `direction_id` varchar(10) DEFAULT NULL,
  `direction_start_stop` varchar(200) DEFAULT NULL COMMENT '该线路的起点站',
  `direction_end_stop` varchar(200) DEFAULT NULL COMMENT '该线路的终点站',
  `earliest_departure_time` varchar(100) DEFAULT NULL COMMENT '该线路最早发车时间点',
  `lastest_departure_time` varchar(100) DEFAULT NULL COMMENT '该线路最晚发车时间点',
  PRIMARY KEY (`line_info_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `bus_info` (
  `bus_info_id` int(16) unsigned NOT NULL AUTO_INCREMENT,
  `create_time` timestamp NULL DEFAULT NULL,
  `modify_time` timestamp NULL DEFAULT NULL,
  `bus_name` varchar(500) DEFAULT NULL,
  `is_favour` int(2) DEFAULT NULL COMMENT '0=>false; 1=> true',
  KEY `bus_info_id` (`bus_info_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#v1 end
