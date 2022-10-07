import json
from pickle import TRUE
from unicodedata import name
from flask_restx import Resource 
from flask import jsonify, request, redirect

# 비밀번호 암호화할 때 필요함
from Crypto.Cipher import AES
from secrets import token_bytes

import datetime 

from database.db import *

class Password_encryption:
    # 인코딩
    def encoding(self, user_pw):
        key = token_bytes(16)
        
        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(user_pw.encode('ascii'))
        return nonce, ciphertext, tag, key
    
    # 디코딩    
    def decoding(self,user_pw1,user_pw2,user_pw3,key):
        cipher = AES.new(key, AES.MODE_EAX, nonce=user_pw1)
        plaintext = cipher.decrypt(user_pw2)
        try:
            cipher.verify(user_pw3)
            return plaintext.decode('ascii')
        except:
            return False

class userJoin(Resource):
    def get(self,id,pw):  
        password_encryption = Password_encryption()
        # MySQL Server connect
        cur = conn.cursor()
        
        # inquiry
        # MySQL commend implement
        cur.execute("SELECT * FROM user")
        # all row를 가져옴
        res = cur.fetchall()
        
        # user id 조회
        for i in res:
            if (i[0] == id):
                # 비밀번호 인코딩
                user_pw1 = i[1]
                user_pw2 = i[2]
                user_pw3 = i[3]
                key = i[4]
                newPw = password_encryption.decoding(user_pw1,user_pw2,user_pw3,key)
                if(newPw == pw):
                    return "TRUE"
                break
        return "FALSE"
    
class userMembership(Resource):
    def get(self, id):
        password_encryption = Password_encryption()
        
        # MySQL Server connect
        cur = conn.cursor()
        
        # inquiry
        # MySQL commend implement
        cur.execute("SELECT * FROM user")
        # all row를 가져옴
        res = cur.fetchall()
        
        pw = ''
        name = ''
        nickname = ''
        email = ''
        phone = ''
        joinMembershipDate = ''
        # user id 조회
        for i in res:
            if (i[0] == id):
                # 비밀번호 인코딩
                user_pw1 = i[1]
                user_pw2 = i[2]
                user_pw3 = i[3]
                key = i[4]
                pw = password_encryption.decoding(user_pw1,user_pw2,user_pw3,key)
                
                name = i[5]
                nickname = i[6]
                email = i[7]
                phone = i[8]
                joinMembershipDate = i[9]
                
        return jsonify(id,pw,name,nickname,email,phone,joinMembershipDate)
        
    def post(self):
        password_encryption = Password_encryption()
        
        id = request.json['id']
        pw = request.json['pw']
        name = request.json['name']
        nickname = request.json['nickname']
        email = request.json['email']
        phone = request.json['phone']
        
        # 비밀번호 인코딩
        pw1,pw2,pw3, pwKey = password_encryption.encoding(pw)
        
        # MySQL Server connect
        cur = conn.cursor()
        
        # user add
        # MySQL user table values add
        sql = "insert into user values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        # datetime
        DT = datetime.datetime.today()
        user_date = DT.strftime('%Y/%m/%d %H:%M:%S')
        
        vals = (id, pw1, pw2, pw3, pwKey, name, nickname, email, phone, user_date)
        cur.execute(sql,vals)
        conn.commit()
        
class allHooverInfo(Resource):
    def get(self,id):
        # MySQL sever connect
        cur = conn.cursor()
        
        # inquiry
        sql = "SELECT * FROM roomInfo WHERE roomNumber in ((SELECT roomNumber FROM room WHERE id = %s))"
        vals = id
        
        print(sql,vals);
        # 쿼리 삽입
        cur.execute(sql,vals)

        # 모든 결과값을 가져옴
        res = cur.fetchall()
        
        return jsonify(res)
    
class hooverInfo(Resource):
    def get(self,id,roomNumber):
        # MySQL sever connect
        cur = conn.cursor()
        
        # inquiry
        sql = "SELECT * FROM roomInfo WHERE roomNumber = (SELECT roomNumber FROM room WHERE id = %s and roomNumber = %s)"
        vals = (id,roomNumber)
        
        print(sql,vals);
        # 쿼리 삽입
        cur.execute(sql,vals)

        # 모든 결과값을 가져옴
        res = cur.fetchall()
        
        return jsonify(res)
    
class hooverSpecificInfo(Resource):
    def get(self,id,roomName,startDate,endDate):
        # MySQL sever connect
        cur = conn.cursor()
        
        # inquiry
        sql = "SELECT * FROM roomInfo WHERE roomNumber = ((SELECT roomNumber FROM room WHERE id = %s and roomName = %s) and date(uploadTime) between %s and %s)"
        vals = (id,roomName,startDate,endDate)
        
        print(sql,vals);
        # 쿼리 삽입
        cur.execute(sql,vals)

        # 모든 결과값을 가져옴
        res = cur.fetchall()
        return jsonify(res)
        