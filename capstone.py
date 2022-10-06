import os
import sys
from flask import Flask, jsonify, request, redirect
from flask_restx import Api, Resource 
from flask_cors import CORS

sys.path.append("C:\\vsCode\pcuCapstoneProject\server\serverToAndroid")
from serverToAndroid import *
sys.path.append("C:\\vsCode\pcuCapstoneProject\server\serverToWeb")
from serverToWeb import *

# Flask 객체 인스턴스 생성
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api = Api(app) 

# android method attach
api.add_resource(userJoin, "/user-join/<string:userid>/<string:userpw>")    
api.add_resource(userMembership, "/joinMembership/<string:id>")    
api.add_resource(userMembership, "/joinMembership")    

# web method attach

# TODO http -> https 변환해서 접속
@app.before_request
def before_request():
    scheme = request.headers.get('X-Forwarded-Proto')
    if scheme and scheme == 'http' and request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

# 코드 수정시 자동 반영
if __name__ == "__main__":
    # 203.250.133.144:8080 / ssl 인증서 등록
    app.run(debug=True, host='203.250.133.144', port=8080, ssl_context=('C:\\vsCode\pcuCapstoneProject\server\ssl\\cert.pem', 'C:\\vsCode\pcuCapstoneProject\server\ssl\key.pem'))