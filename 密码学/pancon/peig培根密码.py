#!/usr/Bin/env python
# -*- coding: utf-8 -*-

#培根解密
#author: bp404

def peig(m):
	Bacon = {
	'AAAAA' : 'A' ,
	'AAAAB' : 'B' ,
	'AAABA' : 'C' ,
	'AAABB' : 'D' ,
	'AABAA' : 'E' ,
	'AABAB' : 'F' ,
	'AABBA' : 'G' ,
	'AABBB' : 'H' ,
	'ABAAA' : 'I' ,
	'ABAAB' : 'J' ,
	'ABABA' : 'K' ,
	'ABABB' : 'L' ,
	'ABBAA' : 'M' ,
	'ABBAB' : 'N' ,
	'ABBBA' : 'O' ,
	'ABBBB' : 'P' ,
	'BAAAA' : 'Q' ,
	'BAAAB' : 'R' ,
	'BAABA' : 'S' ,
	'BAABB' : 'T' ,
	'BABAA' : 'U' ,
	'BABAB' : 'V' ,
	'BABBA' : 'W' ,
	'BABBB' : 'X' ,
	'BBAAA' : 'Y' ,
	'BBAAB' : 'Z' 
	}
	output = ''
	for i in range(0, len(m) - 4, 5):
		temp = m[i: i + 5]
		output += Bacon[temp]
	return output
m = raw_input("Input cipher text:")
print "After decryption for:" + peig(m)




