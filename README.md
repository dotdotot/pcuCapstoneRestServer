# Projects
# Flask-RestApi Server
🗓 프로젝트 소개 : Flask RestApi Server</br>
🗓 기간 : 2022.10.03 ~   </br>
🗓 팀원:  [준석](https://github.com/dotdotot)</br>
🗓 리뷰어: [준석](https://github.com/dotdotot)</br></br>

# 사전준비
##  Flask 설치</br>
<pre>
<code>
$ pip install flask
</pre>
</code>
from flask import Flask, jsonify, request, redirect</br></br>

## rest api </br>
from flask_restx import Api, Resource</br>
from flask_cors import CORS</br></br>

## mysql 설치 </br>
import pymysql</br></br>

## ssl 인증서 (OpenSSL) </br>
모든 인증서는 발급기관(CA)가 있어야 하나, 최상위에 있는 인증기관(root ca)은 서명해줄 상위 인증기관이 없으므로 root ca의 개인키로 스스로의 인증서에 서명하여 최상위 인증기관 인증서를 만든다.

## openssl</br>

* openssl 설치</br>
<pre>
<code>
yum install -y openssl
</pre>
</code>

* openssl 버전 확인</br>
openssl</br>

* CA 개인키 생성</br>
openssl genrsa -out rootCA.key 2048</br>
(Ros알고리즘을 사용하여 2048bit 길이의 CA 개인키 생성)</br>

* CA CSR 생성하기</br>
CSR - 인증 서명 요청으로써 인증서를 발급하는데 필요한 키</br>
oepnssl 명령어 관련 사이트 (https://www.openssl.org/docs/manmaster/man1/)

# 백앤드 쿼리 및  뷰 
## web</br>

## android</br>
* Password_encryption (비밀번호 암호화)
* userJoin (get)
- 사용자에게 id와 pw를 입력받고 해당 아이디가 존재하는지 확인, 비밀번호를 인코딩하고 동일한지 확인한 후 동일하다면 ok 메세지 return
* userMembership (get,post)
- get방식은 사용자에 대한 모든 정보를 get해오는데 사용</br>
json head부분에 사용자 아이디를 추가로 입력받고 해당 아이디가 존재한다면 id, pw, name, nickname, email, phone, joinMembershipDate를 return
- post방식은 사용자에게 id, pw, name, nickname, email, phone, joinMembershipDate를 json body로 받고 db에 올림 (비밀번호는 암호화진행)
(동일한 아이디가 존재하는지는 안드로이드에서 확인 or 서버에서 추가 메소드 제작)

# 백인드 사용한  프레임 워크 
* Flask
* rest-api
* mysql
* logging

# 데이터베이스 테이블 설계
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

* 데이터베이스 중요한 점
* user 테이블에서 비밀번호가 여러개며 key를 가지고 있는 이유는 암호화를 진행했기 때문
* 그렇기에 varchar타입이 아닌 바이너리 타입으로 저장해야함 tinyblob형식으로 저장

# 사용한 라이브러리
* os
* Flask, jsonify, request, redirect
* Api, Resource
* CORS
* pymysql
* datetime
* logging, logging.config

# 사용할 협업툴 

# Commit 규칙
> 커밋 제목은 최대 50자 입력 </br>
본문은 한 줄 최대 72자 입력 </br>
Commit 메세지 </br>

🪛[chore]: 코드 수정, 내부 파일 수정. </br>
✨[feat]: 새로운 기능 구현. </br>
🎨[style]: 스타일 관련 기능.(코드의 구조/형태 개선) </br>
➕[add]: Feat 이외의 부수적인 코드 추가, 라이브러리 추가 </br>
🔧[file]: 새로운 파일 생성, 삭제 시 </br>
🐛[fix]: 버그, 오류 해결. </br>
🔥[del]: 쓸모없는 코드/파일 삭제. </br>
📝[docs]: README나 WIKI 등의 문서 개정. </br>
💄[mod]: storyboard 파일,UI 수정한 경우. </br>
✏️[correct]: 주로 문법의 오류나 타입의 변경, 이름 변경 등에 사용합니다. </br>
🚚[move]: 프로젝트 내 파일이나 코드(리소스)의 이동. </br>
⏪️[rename]: 파일 이름 변경이 있을 때 사용합니다. </br>
⚡️[improve]: 향상이 있을 때 사용합니다. </br>
♻️[refactor]: 전면 수정이 있을 때 사용합니다. </br>
🔀[merge]: 다른브렌치를 merge 할 때 사용합니다. </br>
✅ [test]: 테스트 코드를 작성할 때 사용합니다. </br>







