# -*- coding: utf-8 -*-
'如果重复字段差有公因子，则输出公因子列表。若无，输出一个二维列表，每维第一个元素表示重复字段差的因子，第二个元素表示拥有此因子的字段差总数。'
def GCD(step):
	gcd_list=[]
	buf=[]
	if not len(step):
		return "None has ben found"
	else:#find GCD
		if min(step)>len(step)/8:
			step_min=min(step)
		else:
			step_min=len(step)/8
		for con in xrange(2,step_min+1):
			flag=True
			for each_step in step:
				if each_step%con:
					flag=False
					break
			if flag:
				gcd_list.append(con)
	if len(gcd_list):
		return gcd_list
	else:#find GCD list
		for con in xrange(2,step_min+1):
			gcd_list.append([con,0])
			for each_step in step:
				if each_step%con:
					gcd_list[con-2][1]-=1
		for each in gcd_list:
			each[1]+=len(step)
			if each[1]:
				buf.append(each)
		for i in xrange(1,len(buf)):
			j=i
			while j>0:
				if buf[j][1]<buf[j-1][1]:
					tem=buf[j-1]
					buf[j-1]=buf[j]
					buf[j]=tem
				j-=1
		return buf


def kasiski():
	f=open("./sec.txt")
	sec_msg="".join(f.readlines())
	step=[]
	flag=False
	lenth=len(sec_msg)
	for i in xrange(lenth-5):
		for j in xrange(i+3,lenth-2):
			if sec_msg[i]==sec_msg[j] and sec_msg[i+1]==sec_msg[j+1] and sec_msg[i+2]==sec_msg[j+2]:
				# print sec_msg[i:i+5]
				# print sec_msg[j:j+5]
				# print i,j,j-i
				flag=True
				step.append(j-i)
		if flag:
			i+=3
#	print step
	print GCD(step)
	

if __name__ == '__main__':
	kasiski()