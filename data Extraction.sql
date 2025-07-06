CREATE DATABASE phonepe_data;
SELECT * FROM aggregated_transaction LIMIT 10;
SHOW DATABASES;
USE phonepe;
SHOW TABLES;

CREATE TABLE aggregated_user (
    state VARCHAR(50),
    year INT,
    quarter INT,
    registered_users BIGINT,
    app_opens BIGINT
);

CREATE TABLE aggregated_insurance (
    state VARCHAR(50),
    year INT,
    quarter INT,
    insurance_type VARCHAR(50),
    insurance_count BIGINT,
    insurance_amount DOUBLE
);


CREATE TABLE map_transaction (
    state VARCHAR(50),
    year INT,
    quarter INT,
    district VARCHAR(100),
    transaction_count BIGINT,
    transaction_amount DOUBLE
);

CREATE TABLE map_user (
    state VARCHAR(50),
    year INT,
    quarter INT,
    district VARCHAR(100),
    registered_users BIGINT
);

CREATE TABLE map_insurance (
    state VARCHAR(50),
    year INT,
    quarter INT,
    district VARCHAR(100),
    insurance_type VARCHAR(50),
    insurance_count BIGINT,
    insurance_amount DOUBLE
);

CREATE TABLE top_transaction (
    state VARCHAR(50),
    year INT,
    quarter INT,
    pincode VARCHAR(20),
    transaction_type VARCHAR(50),
    transaction_count BIGINT,
    transaction_amount DOUBLE
);

CREATE TABLE top_user (
    state VARCHAR(50),
    year INT,
    quarter INT,
    pincode VARCHAR(20),
    registered_users BIGINT
);

CREATE TABLE top_insurance (
    state VARCHAR(50),
    year INT,
    quarter INT,
    pincode VARCHAR(20),
    insurance_type VARCHAR(50),
    insurance_count BIGINT,
    insurance_amount DOUBLE
);

SELECT * FROM aggregated_transaction LIMIT 10;
SELECT * FROM aggregated_user LIMIT 10;

SELECT COUNT(*) FROM aggregated_insurance;
SELECT * FROM aggregated_insurance LIMIT 10;

SELECT COUNT(*) FROM aggregated_transaction;
SELECT * FROM aggregated_transaction LIMIT 5;


SELECT COUNT(*) FROM top_insurance;
SELECT * FROM top_insurance LIMIT 5;

SELECT COUNT(*) FROM top_insurance;
SELECT * FROM top_user LIMIT 5;

DESCRIBE top_insurance;

DROP TABLE IF EXISTS top_insurance;

CREATE TABLE top_insurance_new (
    state VARCHAR(50),
    year INT,
    quarter INT,
    pincode VARCHAR(20),
    insured_users BIGINT
);


SELECT COUNT(*) FROM top_insurance_new;
SELECT * FROM top_insurance_new LIMIT 5;

show databases;
use phonepe;


DROP TABLE IF EXISTS top_insurance;

DROP TEMPORARY TABLE IF EXISTS top_insurance;

TRUNCATE TABLE top_insurance;
RENAME TABLE top_insurance_new TO top_insurance;