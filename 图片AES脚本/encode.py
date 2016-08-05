#!/usr/bin/env python

import image
import sys
from Crypto.Cipher import AES

#im1 = Image.open("flag.png")
f1 = open('text.bmp','rb')

key='bestwing12345678'

obj = AES.new(key, AES.MODE_ECB)
rawdata = f1.read()
head = rawdata[0:0x36]
imdata = rawdata[0x36:]
while (len(imdata)%16!=0): 
	imdata += '\x00';
f1.close()
after = obj.encrypt(imdata)


f2 = open('out.bmp','wb')
f2.write(after)
f2.close();
