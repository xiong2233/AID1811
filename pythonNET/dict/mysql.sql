create table user(
    id int primary key auto_increment,
    name varchar(32) not null,
    password varchar(32) default '000000'
)default charset=utf8;

create table hist(
    id int primary key auto_increment,
    name varchar(32)not null,
    word VARCHAR(32) not null,
    time VARCHAR(64)
)default charset=utf8;

create table words(
    id int PRIMARY KEY auto_increment,
    word VARCHAR(32),
    interpret text
) default charset=utf8;