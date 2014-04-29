CREATE TABLE `sensor_readings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reading_ts` datetime DEFAULT NULL,
  `sensor_location` varchar(45) DEFAULT NULL,
  `sensor_type` varchar(45) DEFAULT NULL,
  `sensor_value` decimal(8,2) DEFAULT NULL,
  `create_user` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_reading_ts_type` (`reading_ts`,`sensor_type`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
