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