import os
from flask import Flask, jsonify, request, redirect
from flask_restx import Api, Resource 
from flask_cors import CORS
import pymysql  # mysql 
import datetime # python datetime

# logging
import logging
import logging.config

# Flask 객체 인스턴스 생성
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api = Api(app) 

# mysql setting
conn = pymysql.connect(host='203.250.133.144', user='dotdotot', password='!wnstjr4428', db='my_db', charset='utf8')

# 코드 수정시 자동 반영
if __name__ == "__main__":
    # 203.250.133.144:8080 / ssl 인증서 등록
    app.run(debug=True, host='203.250.133.144', port=8080, ssl_context=('C:\\vsCode\pcuCapstoneProject\server\ssl\\cert.pem', 'C:\\vsCode\pcuCapstoneProject\server\ssl\key.pem'))