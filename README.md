Flask-RestApi Server

# Flask-RestApi Server


## Projects
## Flask-RestApi Server
🗓 프로젝트 소개 : Flask RestApi Server</br>
🗓 기간 : 2022.10.03 ~   </br>
🗓 팀원:  [준석](https://github.com/dotdotot)</br>
🗓 리뷰어: [준석](https://github.com/dotdotot)

## 사전준비
- Flask 설치</br>
    $ pip install flask </br>
from flask import Flask, jsonify, request, redirect
- rest api </br>
from flask_restx import Api, Resource 
from flask_cors import CORS
- mysql 설치 </br>
import pymysql  # mysql 
- ssl 인증서 (OpenSSL) </br>
모든 인증서는 발급기관(CA)가 있어야 하나, 최상위에 있는 인증기관(root ca)은 서명해줄 상위 인증기관이 없으므로 root ca의 개인키로 스스로의 인증서에 서명하여 최상위 인증기관 인증서를 만든다.
(1)openssl 설치
'''
yum install -y openssl
'''
(2)openssl 버전 확인
openssl
(3)CA 개인키 생성
openssl genrsa -out rootCA.key 2048
(Ros알고리즘을 사용하여 2048bit 길이의 CA 개인키 생성)
(4)CA CSR 생성하기
CSR - 인증 서명 요청으로써 인증서를 발급하는데 필요한 키

oepnssl 명령어 관련 사이트 (https://www.openssl.org/docs/manmaster/man1/)

## 앱아이콘 

## 웹 뷰ui

## 백앤드 쿼리 및  뷰 

## 백인드 사용한  프레임 워크 

## 웹 사용한 프레임 워크

## 사용한 라이브러리

## 사용할 협업툴 

## Commit 규칙
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

### Commit Body 규칙
> 제목 끝에 마침표(.) 금지 </br>
한글로 작성 </br>
브랜치 이름 규칙

- `STEP1`, `STEP2`, `STEP3`






