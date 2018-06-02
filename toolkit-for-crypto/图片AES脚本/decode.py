# -*- coding: utf-8 -*-

from Crypto.Cipher import AES

KEY='bestwing12345678'
cipher=AES.new(KEY)
f = open('bestwing12345678.bmp','rb')
data=f.read()

decrypted = cipher.decrypt(data)
f1 = open('123.bmp','wb')
f1.write(decrypted)
f1.close()
