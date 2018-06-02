#!/usr/Bin/env python
# -*- coding: utf-8 -*-

#栅栏解密
#author: bp404

result ={0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:'',11:'',12:'',13:'',14:'',15:'',16:'',17:''};
b = 17;
s = "tn c0afsiwal kes,hwit1r  g,npt  ttessfu}ua u  hmqik e {m,  n huiouosarwCniibecesnren."
for i in range(len(s)):
    a = i%b;
    result.update({a:result[a]+s[i]});
for i in range(b):
    print result[i];
