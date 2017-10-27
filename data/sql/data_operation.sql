
-- mysql -u root --show-warninings -p

-- SOURCE /home/epcc/proj/tianchi/data/sql/data_operation.sql

-- CREATE DATABASE commerce

USE commerce

SELECT 'Creating tables' AS '';
CREATE TABLE shops (id INT, category_id INT, longitude FLOAT(10,6), latitude FLOAT(10,6), 
	price INT, mall_id INT, PRIMARY KEY(id));

CREATE TABLE train_infos (id INT, user_id INT, shop_id INT, time_stamp DATETIME, 
	longitude FLOAT(10,6), latitude FLOAT(10,6), PRIMARY KEY(id));

CREATE TABLE test_infos (id INT, user_id INT, mall_id INT, time_stamp DATETIME,  
	longitude FLOAT(10,6), latitude FLOAT(10,6), PRIMARY KEY(id));

CREATE TABLE wifi_infos_train (id INT, wifi_id INT, signal_value INT, connected BIT(1), PRIMARY KEY(id));

CREATE TABLE wifi_infos_test (id INT, wifi_id INT, signal_value INT, connected BIT(1), PRIMARY KEY(id));

CREATE TABLE train_and_wifi (train_id INT,  wifi_id INT, PRIMARY KEY (train_id, wifi_id), 
	FOREIGN KEY (train_id) REFERENCES train_infos(id), FOREIGN KEY (wifi_id) REFERENCES wifi_infos_train(id));

CREATE TABLE test_and_wifi (test_id INT, wifi_id INT, PRIMARY KEY (wifi_id), 
	FOREIGN KEY (test_id) REFERENCES test_infos(id), FOREIGN KEY (wifi_id) REFERENCES wifi_infos_test(id));

-- system cd /home/epcc/proj/tianchi/data/output

SELECT 'Insert shops' AS '';
LOAD DATA LOCAL INFILE '/home/epcc/proj/tianchi/data/output/shops.csv' INTO TABLE shops;

SELECT 'Insert train_infos' AS '';
LOAD DATA LOCAL INFILE '/home/epcc/proj/tianchi/data/output/train_infos.csv' INTO TABLE train_infos;
SELECT 'Insert wifi_infos_train' AS '';
LOAD DATA LOCAL INFILE '/home/epcc/proj/tianchi/data/output/wifi_infos_train.csv' INTO TABLE wifi_infos_train 
	(id, wifi_id, signal_value, @connected_var) set connected=cast(@connected_var as signed);
SELECT 'Insert train_and_wifi' AS '';
LOAD DATA LOCAL INFILE '/home/epcc/proj/tianchi/data/output/train_and_wifi.csv' INTO TABLE train_and_wifi;

SELECT 'Insert test_infos' AS '';
LOAD DATA LOCAL INFILE '/home/epcc/proj/tianchi/data/output/test_infos.csv' INTO TABLE test_infos;
SELECT 'Insert wifi_infos_test' AS '';
LOAD DATA LOCAL INFILE '/home/epcc/proj/tianchi/data/output/wifi_infos_test.csv' INTO TABLE wifi_infos_test 
	(id, wifi_id, signal_value, @connected_var) set connected=cast(@connected_var as signed);
SELECT 'Insert test_and_wifi' AS '';
LOAD DATA LOCAL INFILE '/home/epcc/proj/tianchi/data/output/test_and_wifi.csv' INTO TABLE test_and_wifi;



-- DROP TABLE shops;

-- DROP TABLE train_and_wifi;
-- DROP TABLE wifi_infos_train;
-- DROP TABLE train_infos;

-- DROP TABLE test_and_wifi;
-- DROP TABLE wifi_infos_test;
-- DROP TABLE test_infos;

SELECT COUNT(*) FROM (
	SELECT DISTINCT A.longitude, A.latitude FROM test_infos A) AS R;


SELECT MIN(longitude), MAX(longitude), MIN(latitude), MAX(latitude) FROM test_infos;
SELECT MIN(longitude), MAX(longitude), MIN(latitude), MAX(latitude) FROM train_infos WHERE longitude >= 80 AND latitude >= 20;

SELECT MIN(longitude), MAX(longitude), MIN(latitude), MAX(latitude) FROM shops;



SELECT COUNT(DISTINCT user_id) FROM test_infos WHERE user_id NOT IN (SELECT user_id FROM train_infos);

SELECT COUNT(DISTINCT user_id) FROM test_infos;


SELECT COUNT(DISTINCT wifi_id) FROM wifi_infos_test WHERE wifi_id NOT IN (SELECT wifi_id FROM wifi_infos_train);

SELECT COUNT(DISTINCT wifi_id) FROM wifi_infos_test;


SELECT COUNT(DISTINCT longitude) FROM test_infos WHERE longitude NOT IN (SELECT longitude FROM train_infos) 
	AND longitude NOT IN (SELECT longitude FROM shops);
SELECT COUNT(DISTINCT longitude) FROM test_infos;



SELECT COUNT(DISTINCT latitude) FROM test_infos WHERE latitude NOT IN (SELECT latitude FROM train_infos) 
	AND latitude NOT IN (SELECT latitude FROM shops);
SELECT COUNT(DISTINCT latitude) FROM test_infos;


SELECT COUNT(*) FROM test_infos WHERE longitude NOT IN (SELECT longitude FROM train_infos) 
	AND longitude NOT IN (SELECT longitude FROM shops) AND latitude NOT IN (SELECT latitude FROM train_infos) 
	AND latitude NOT IN (SELECT latitude FROM shops);
