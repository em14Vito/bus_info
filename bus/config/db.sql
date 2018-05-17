# v1 start
# time : 2018年05月06日18:55:17

CREATE TABLE `stop_real_time_msg` (
  `stop_real_time_id` INT(16) UNSIGNED NOT NULL AUTO_INCREMENT,
  `stop_info_id` INT(16) UNSIGNED NOT NULL ,
  `create_time` TIMESTAMP NULL DEFAULT NULL,
  `modify_time` TIMESTAMP NULL DEFAULT NULL,
  `car_name` VARCHAR(100) DEFAULT NULL,
  `distance` INT(20) DEFAULT NULL COMMENT '车距离该站点距离多远 , 单位 米',
  `remain_time` INT(20) DEFAULT NULL COMMENT '大约还剩下多少时间,单位 秒',
  `remain_stop` INT(20) DEFAULT NULL COMMENT '大约还剩下多少个站点, ',
  PRIMARY KEY (`stop_real_time_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;


CREATE TABLE `stop_info` (
  `stop_info_id` INT(16) UNSIGNED NOT NULL AUTO_INCREMENT,
  `create_time` TIMESTAMP NULL DEFAULT NULL,
  `modify_time` TIMESTAMP NULL DEFAULT NULL,
  `line_info_id` INT(16) DEFAULT NULL COMMENT '关联线路信息id',
  `stop_id` VARCHAR(30) DEFAULT NULL,
  `stop_name` VARCHAR(50) DEFAULT NULL,
  `is_favour` INT(2) DEFAULT NULL COMMENT '0=>false; 1=> true',
  PRIMARY KEY (`stop_info_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;


CREATE TABLE `line_info` (
  `line_info_id` INT(16) UNSIGNED NOT NULL AUTO_INCREMENT,
  `create_time` TIMESTAMP NULL DEFAULT NULL,
  `modify_time` TIMESTAMP NULL DEFAULT NULL,
  `bus_info_id` INT(16) DEFAULT NULL COMMENT '外键关联bus',
  `direction_id` VARCHAR(10) DEFAULT NULL,
  `direction_start_stop` VARCHAR(200) DEFAULT NULL COMMENT '该线路的起点站',
  `direction_end_stop` VARCHAR(200) DEFAULT NULL COMMENT '该线路的终点站',
  `earliest_departure_time` VARCHAR(100) DEFAULT NULL COMMENT '该线路最早发车时间点',
  `lastest_departure_time` VARCHAR(100) DEFAULT NULL COMMENT '该线路最晚发车时间点',
  PRIMARY KEY (`line_info_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE `bus_info` (
  `bus_info_id` INT(16) UNSIGNED NOT NULL AUTO_INCREMENT,
  `create_time` TIMESTAMP NULL DEFAULT NULL,
  `modify_time` TIMESTAMP NULL DEFAULT NULL,
  `bus_id` VARCHAR(500) DEFAULT NULL,
  `bus_name` VARCHAR(500) DEFAULT NULL,
  KEY `bus_info_id` (`bus_info_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;


#v1 end
