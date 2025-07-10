CREATE DATABASE phonepe;
SHOW DATABASES;
USE phonepe;
SHOW TABLES;

CREATE TABLE aggregated_transaction (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(50),
    year INT,
    quarter INT,
    transaction_type VARCHAR(50),
    transaction_count BIGINT,
    transaction_amount DOUBLE
);


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
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(50),
    year INT,
    quarter INT,
    district VARCHAR(100),
    insured_users BIGINT
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
    insured_users BIGINT
);

SELECT * FROM aggregated_transaction LIMIT 10;
SELECT * FROM aggregated_user LIMIT 10;

SELECT COUNT(*) FROM aggregated_insurance;

SELECT * FROM aggregated_insurance LIMIT 10;

SELECT * FROM map_user LIMIT 10;
SELECT COUNT(*) FROM map_user;

SELECT * FROM map_insurance LIMIT 10;
SELECT COUNT(*) FROM map_insurance;

SELECT * FROM top_transaction LIMIT 10;
SELECT COUNT(*) FROM top_transaction;

SELECT * FROM top_user LIMIT 10;
SELECT COUNT(*) FROM top_user;

SELECT * FROM top_insurance LIMIT 10;
SELECT COUNT(*) FROM top_insurance;

use phonepe;
 
SELECT COUNT(*)  FROM map_user	;




