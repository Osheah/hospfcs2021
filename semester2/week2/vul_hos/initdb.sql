create database if not exists cwe; 
use cwe;

create table forms (
    id int NOT NULL AUTO_INCREMENT,
    first_name varchar(250),
    last_name varchar(250),
    email varchar(250),
    comment varchar (250),
    PRIMARY KEY (id) 
    );

    -- for dropping in the sql injection  '; drop table test;
create table test (
    id int NOT NULL AUTO_INCREMENT,
    testdata varchar(250),
    PRIMARY KEY (id) 
    );