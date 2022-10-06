import pymysql  # mysql 

# mysql setting
conn = pymysql.connect(host='203.250.133.144', user='capstone', password='!wnstjr4428', db='capstone_database', charset='utf8')

# create table user (
# id varchar(20) not null unique primary key,
# pw1 tinyblob not null,
# pw2 tinyblob not null,
# pw3 tinyblob not null,
# pwKey tinyblob not null,
# name varchar(5) not null,
# nickname varchar(10) not null unique,
# email varchar(30) not null,
# phone varchar(13) not null,
# joinMembershipDate datetime not null
# )engine = InnoDB default charset=utf8mb4;

# create table room (
# roomNumber int(2) not null unique primary key,
# roomName varchar(10) not null,
# id varchar(20) not null unique,
# foreign key(id) references user(id) on update cascade on delete cascade
# );

# create table roomInfo(
# roomNumber int(2) not null unique,
# uploadTime datetime not null,
# color varchar(3) not null,
# temperature float not null,
# humidity float not null,
# fineDust float not null,
# foreign key(roomNumber) references room(roomNumber) on update cascade on delete cascade
# )