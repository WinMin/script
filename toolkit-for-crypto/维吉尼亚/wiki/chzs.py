# -*- coding: utf-8 -*-
import string
Alphabet_boom=[0.082,0.015,0.028,0.043,0.127,0.022,0.020,0.061,0.070,0.002,0.008,0.040,0.024,0.067,0.075,0.019,0.001,0.060,0.063,0.091,0.028,0.010,0.023,0.001,0.020,0.001]

def confram(sec_msg,lenth,word):
	Ic=[0 for i in range(lenth)]


	for con in xrange(lenth):
		f=[0.0 for i in range(26)]

		for i in xrange(len(word[con])):#统计频数
			f[ord(word[con][i])-ord("a")]+=1

		tem=0.0
		for i in xrange(26):
			if f[i] <1:
				pass
			else:
				tem+=f[i]*(f[i]-1)
		Ic[con]=tem/(len(word[con])*(len(word[con])-1))

	print "Expectation: 0.065601\nIc =",
	print Ic
	print "\n\n"

def boom(sec_msg,lenth,word):
	Mg=[[0.0 for i in xrange(26)] for j in xrange(lenth)]
	#遍历key分组lenth
	for group in xrange(lenth):
		#统计频数
		f=[0.0 for i in xrange(26)]
		for i in xrange(len(word[group])):
			f[ord(word[group][i])-ord("a")]+=1
		#遍历分组内key26
		for key in xrange(26):
			#遍历word内第lenth个分组字符串，计算 Mg[lenth][key26]=累加fp/n'
			for each in xrange(26):
				Mg[group][key]+=f[(each+key)%26]*Alphabet_boom[each]/len(word[group])
	key=""
	for i in xrange(lenth):
		flag=False
		for j in xrange(26):
			if Mg[i][j]<0.05:
				continue
			flag=True
			key+=chr(j+ord("a"))
			print chr(j+ord("a"))+"-->",
			print Mg[i][j],
			print "     "
		if not flag:
			print "none!"
			key+=" "
	print "key>>",key
def chzs():
	f=open("./sec.txt")
	sec_msg_temp="".join(f.readlines())
	f.close()
	sec_msg=""
	lenth=int(raw_input("lenth\n"))
	for each in sec_msg_temp:
		if each in string.letters:
			sec_msg+=each

	word=["" for i in range(lenth)]
	for i in xrange(len(sec_msg)):
		word[i%lenth]+=sec_msg[i]#按key长分组

	confram(sec_msg,lenth,word)
	boom(sec_msg,lenth,word)

if __name__ == '__main__':
	chzs()