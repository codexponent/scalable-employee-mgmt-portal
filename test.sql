CREATE TABLE employee(  
    id int NOT NULL primary key AUTO_INCREMENT comment 'primary key',
    first_name varchar(255) ,
    last_name varchar(255) ,
    company varchar(255) ,
    position varchar(255) ,
    phone varchar(255) ,
    email varchar(255) ,
    country varchar(255)
) default charset utf8 comment '';
