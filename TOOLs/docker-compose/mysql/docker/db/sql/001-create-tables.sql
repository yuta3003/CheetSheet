---- drop ----
DROP TABLE IF EXISTS `test_table`;

---- create ----
CREATE TABLE IF NOT EXISTS `test_table`
(
`id`          INT(20) AUTO_INCREMENT,
`name`        VARCHAR(20) NOT NULL,
`createed_at` DATETIME DEFAULT NULL,
`updated_at`  DATETIME DEFAULT NULL,
PRIMARY KEY ('id')
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
