# Projects
# Flask-RestApi Server
๐ ํ๋ก์ ํธ ์๊ฐ : Flask RestApi Server</br>
๐ ๊ธฐ๊ฐ : 2022.10.03 ~   </br>
๐ ํ์:  [์ค์](https://github.com/dotdotot)</br>
๐ ๋ฆฌ๋ทฐ์ด: [์ค์](https://github.com/dotdotot)</br></br>

# ์ฌ์ ์ค๋น
##  Flask ์ค์น</br>
<pre>
<code>
$ pip install flask
</pre>
</code>
from flask import Flask, jsonify, request, redirect</br></br>

## rest api </br>
from flask_restx import Api, Resource</br>
from flask_cors import CORS</br></br>

## mysql ์ค์น </br>
import pymysql</br></br>

## ssl ์ธ์ฆ์ (OpenSSL) </br>
๋ชจ๋  ์ธ์ฆ์๋ ๋ฐ๊ธ๊ธฐ๊ด(CA)๊ฐ ์์ด์ผ ํ๋, ์ต์์์ ์๋ ์ธ์ฆ๊ธฐ๊ด(root ca)์ ์๋ชํด์ค ์์ ์ธ์ฆ๊ธฐ๊ด์ด ์์ผ๋ฏ๋ก root ca์ ๊ฐ์ธํค๋ก ์ค์ค๋ก์ ์ธ์ฆ์์ ์๋ชํ์ฌ ์ต์์ ์ธ์ฆ๊ธฐ๊ด ์ธ์ฆ์๋ฅผ ๋ง๋ ๋ค.

## openssl</br>

* openssl ์ค์น</br>
<pre>
<code>
yum install -y openssl
</pre>
</code>

* openssl ๋ฒ์  ํ์ธ</br>
openssl</br>

* CA ๊ฐ์ธํค ์์ฑ</br>
openssl genrsa -out rootCA.key 2048</br>
(Ros์๊ณ ๋ฆฌ์ฆ์ ์ฌ์ฉํ์ฌ 2048bit ๊ธธ์ด์ CA ๊ฐ์ธํค ์์ฑ)</br>

* CA CSR ์์ฑํ๊ธฐ</br>
CSR - ์ธ์ฆ ์๋ช ์์ฒญ์ผ๋ก์จ ์ธ์ฆ์๋ฅผ ๋ฐ๊ธํ๋๋ฐ ํ์ํ ํค</br>
oepnssl ๋ช๋ น์ด ๊ด๋ จ ์ฌ์ดํธ (https://www.openssl.org/docs/manmaster/man1/)

# ๋ฐฑ์ค๋ ์ฟผ๋ฆฌ ๋ฐ  ๋ทฐ 
## anduino</br>

## web</br>
* Password_encryption (๋น๋ฐ๋ฒํธ ์ํธํ)
* userJoin (get)
>> ์ฌ์ฉ์์๊ฒ id์ pw๋ฅผ ์๋ ฅ๋ฐ๊ณ  ํด๋น ์์ด๋๊ฐ ์กด์ฌํ๋์ง ํ์ธ, ๋น๋ฐ๋ฒํธ๋ฅผ ์ธ์ฝ๋ฉํ๊ณ  ๋์ผํ์ง ํ์ธํ ํ ๋์ผํ๋ค๋ฉด true ๋ฉ์ธ์ง return</br>
<code>
api.add_resource(userJoin, "/userJoin/<'string:id'>/<'string:pw'>")   
</code></br></br>

* userMembership (get,post)
>> get๋ฐฉ์์ ์ฌ์ฉ์์ ๋ํ ๋ชจ๋  ์ ๋ณด๋ฅผ getํด์ค๋๋ฐ ์ฌ์ฉ</br>
json head๋ถ๋ถ์ ์ฌ์ฉ์ ์์ด๋๋ฅผ ์ถ๊ฐ๋ก ์๋ ฅ๋ฐ๊ณ  ํด๋น ์์ด๋๊ฐ ์กด์ฌํ๋ค๋ฉด id, pw, name, nickname, email, phone, joinMembershipDate๋ฅผ return
>> post๋ฐฉ์์ ์ฌ์ฉ์์๊ฒ id, pw, name, nickname, email, phone, joinMembershipDate๋ฅผ json body๋ก ๋ฐ๊ณ  db์ ์ฌ๋ฆผ (๋น๋ฐ๋ฒํธ๋ ์ํธํ์งํ)</br>
(๋์ผํ ์์ด๋๊ฐ ์กด์ฌํ๋์ง๋ ์๋๋ก์ด๋์์ ํ์ธ or ์๋ฒ์์ ์ถ๊ฐ ๋ฉ์๋ ์ ์)</br>
<code>
api.add_resource(userMembership, "/joinMembership/<'string:id'>")
</code></br>
<code>
api.add_resource(userMembership, "/joinMembership")
</code></br></br>

* hooverInfo (get)
>> ์์ด๋, ๋ฐฉ๋ฒํธ๋ฅผ json head์์ ์๋ ฅ๋ฐ์
>> ํด๋นํ๋ ๋ฐฉ์ ๋ฒํธ, ์๋ก๋ ์๊ฐ, ์๊น, ์จ๋, ์ต๋, ๋ฏธ์ธ๋จผ์ง๋ชจ๋ json bady์ ๊ฐ์ธ์ ๋ฆฌํดํด์ค๋๋ค.
<code>
api.add_resource(hooverInfo, "/hooverInfo/<'string:id'>/<'string:roomNumber'>")   
</code></br></br>

* allHooverInfo (get)
>> ์์ด๋๋ฅผ josn head์ ์๋ ฅ๋ฐ์
>> ํด๋นํ๋ ๋ชจ๋  ๋ฐฉ์์ ๋ํ ์ ๋ณด๋ฅผ return
mysql ์ฟผ๋ฆฌ๋ฌธ</br>
SELECT * FROM roomInfo WHERE roomNumber = ((SELECT roomNumber FROM room WHERE id = "dotdotot" and roomName = "๋ฐฉ3")) and date(uploadTime) between '2022-10-07' and '2023-01-07';</br>
<code>
api.add_resource(allHooverInfo, "/allHooverInfo/<'string:id'>")   
</code></br></br>

* hooverSpecificInfo (get)
>> ์์ด๋, ๋ฐฉ์ด๋ฆ, ์์๋ ์ง, ์ข๋ฃ๋ ์ง๋ฅผ ์๋ ฅ๋ฐ๊ณ  ํด๋นํ๋ ๋ฐฉ์ ์์๋ ์ง์ ์ข๋ฃ๋ ์ง ์ฌ์ด์ ์๋ ๋ชจ๋  ๋ฐ์ดํฐ๋ฅผ returnํด์ค
<code>
api.add_resource(hooverSpecificInfo, "/hooverSpecificInfo/<'string:id'>/<'string:roomName'>/<'string:startDate'>/<'string:endDate'>") 
</code></br></br>

## android</br>
* Password_encryption (๋น๋ฐ๋ฒํธ ์ํธํ)
* userJoin (get)(์น๊ณผ ๋์ผ)
* userMembership (get,post)(์น๊ณผ ๋์ผ)
* hooverInfo (get)(์น๊ณผ ๋์ผ)
* allHooverInfo (get)(์น๊ณผ ๋์ผ)
* hooverSpecificInfo (get) (์น๊ณผ ๋์ผ)

# ๋ฐฑ์ธ๋ ์ฌ์ฉํ  ํ๋ ์ ์ํฌ 
* Flask
* rest-api
* mysql
* logging

# ๋ฐ์ดํฐ๋ฒ ์ด์ค ํ์ด๋ธ ์ค๊ณ
create table user (</br>
id varchar(20) not null unique primary key,</br>
pw1 tinyblob not null,</br>
pw2 tinyblob not null,</br>
pw3 tinyblob not null,</br>
pwKey tinyblob not null,</br>
name varchar(5) not null,</br>
nickname varchar(10) not null unique,</br>
email varchar(30) not null,</br>
phone varchar(13) not null,</br>
joinMembershipDate datetime not null</br>
)engine = InnoDB default charset=utf8mb4;</br></br>

create table room (</br>
roomNumber int(2) not null unique primary key,</br>
roomName varchar(10) not null,</br>
id varchar(20) not null unique,</br>
foreign key(id) references user(id) on update cascade on delete cascade</br>
)engine = InnoDB default charset=utf8mb4;</br></br>

create table roomInfo(</br>
roomNumber int(2) not null unique,</br>
uploadTime datetime not null,</br>
color varchar(3) not null,</br>
temperature float not null,</br>
humidity float not null,</br>
fineDust float not null,</br>
foreign key(roomNumber) references room(roomNumber) on update cascade on delete cascade</br>
)engine = InnoDB default charset=utf8mb4;</br></br>

* ๋ฐ์ดํฐ๋ฒ ์ด์ค ์ค์ํ ์ 
* user ํ์ด๋ธ์์ ๋น๋ฐ๋ฒํธ๊ฐ ์ฌ๋ฌ๊ฐ๋ฉฐ key๋ฅผ ๊ฐ์ง๊ณ  ์๋ ์ด์ ๋ ์ํธํ๋ฅผ ์งํํ๊ธฐ ๋๋ฌธ
* ๊ทธ๋ ๊ธฐ์ varcharํ์์ด ์๋ ๋ฐ์ด๋๋ฆฌ ํ์์ผ๋ก ์ ์ฅํด์ผํจ tinyblobํ์์ผ๋ก ์ ์ฅ

# ์ฌ์ฉํ ๋ผ์ด๋ธ๋ฌ๋ฆฌ
* os
* Flask, jsonify, request, redirect
* Api, Resource
* CORS
* pymysql
* datetime
* logging, logging.config

# ์ฌ์ฉํ  ํ์ํด 

# Commit ๊ท์น
> ์ปค๋ฐ ์ ๋ชฉ์ ์ต๋ 50์ ์๋ ฅ </br>
๋ณธ๋ฌธ์ ํ ์ค ์ต๋ 72์ ์๋ ฅ </br>
Commit ๋ฉ์ธ์ง </br>

๐ช[chore]: ์ฝ๋ ์์ , ๋ด๋ถ ํ์ผ ์์ . </br>
โจ[feat]: ์๋ก์ด ๊ธฐ๋ฅ ๊ตฌํ. </br>
๐จ[style]: ์คํ์ผ ๊ด๋ จ ๊ธฐ๋ฅ.(์ฝ๋์ ๊ตฌ์กฐ/ํํ ๊ฐ์ ) </br>
โ[add]: Feat ์ด์ธ์ ๋ถ์์ ์ธ ์ฝ๋ ์ถ๊ฐ, ๋ผ์ด๋ธ๋ฌ๋ฆฌ ์ถ๊ฐ </br>
๐ง[file]: ์๋ก์ด ํ์ผ ์์ฑ, ์ญ์  ์ </br>
๐[fix]: ๋ฒ๊ทธ, ์ค๋ฅ ํด๊ฒฐ. </br>
๐ฅ[del]: ์ธ๋ชจ์๋ ์ฝ๋/ํ์ผ ์ญ์ . </br>
๐[docs]: README๋ WIKI ๋ฑ์ ๋ฌธ์ ๊ฐ์ . </br>
๐[mod]: storyboard ํ์ผ,UI ์์ ํ ๊ฒฝ์ฐ. </br>
โ๏ธ[correct]: ์ฃผ๋ก ๋ฌธ๋ฒ์ ์ค๋ฅ๋ ํ์์ ๋ณ๊ฒฝ, ์ด๋ฆ ๋ณ๊ฒฝ ๋ฑ์ ์ฌ์ฉํฉ๋๋ค. </br>
๐[move]: ํ๋ก์ ํธ ๋ด ํ์ผ์ด๋ ์ฝ๋(๋ฆฌ์์ค)์ ์ด๋. </br>
โช๏ธ[rename]: ํ์ผ ์ด๋ฆ ๋ณ๊ฒฝ์ด ์์ ๋ ์ฌ์ฉํฉ๋๋ค. </br>
โก๏ธ[improve]: ํฅ์์ด ์์ ๋ ์ฌ์ฉํฉ๋๋ค. </br>
โป๏ธ[refactor]: ์ ๋ฉด ์์ ์ด ์์ ๋ ์ฌ์ฉํฉ๋๋ค. </br>
๐[merge]: ๋ค๋ฅธ๋ธ๋ ์น๋ฅผ merge ํ  ๋ ์ฌ์ฉํฉ๋๋ค. </br>
โ [test]: ํ์คํธ ์ฝ๋๋ฅผ ์์ฑํ  ๋ ์ฌ์ฉํฉ๋๋ค. </br>







