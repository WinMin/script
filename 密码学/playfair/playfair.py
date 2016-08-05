import sys
letters='abcdefghiklmnopqrstuvwxyz'

def gotAlph(preKey):
	key=''
	for x in preKey:
		if 'j'==x:
			key+='i'             #Changeable
		else:
			key+=x
	alph=key
	for x in letters:
		if x in key:
			pass
		else:
			alph+=x
	return alph

def gotCipher(cipher,char_):
	tem_cipher=''
	count=0
	for x in xrange(len(cipher)-1):
		if cipher[x]==cipher[x+1]:
			count+=1
			tem_cipher+=cipher[len(tem_cipher)-count:x+1]
			tem_cipher+=char_
	tem_cipher+=cipher[len(tem_cipher)-count:]
	return tem_cipher

def playfair(key,cipher,char_):
	if char_ in cipher:
		print "bad argv[3]"
	alph=gotAlph(key)
	cipher=gotCipher(cipher,char_)
	plain1=''
	plain2=''
	for t in xrange(len(cipher)/2):
		time1=alph.find(cipher[t*2])
		coor1=[time1/5,time1%5]
		time2=alph.find(cipher[t*2+1])
		coor2=[time2/5,time2%5]
		plain1+=alph[coor1[0]*5+coor2[1]]
		plain1+=alph[coor2[0]*5+coor1[1]]
		plain2+=alph[coor2[0]*5+coor1[1]]
		plain2+=alph[coor1[0]*5+coor2[1]]
	return [plain1,plain2]

if __name__ == '__main__':
	print playfair(sys.argv[1],sys.argv[2],sys.argv[3])