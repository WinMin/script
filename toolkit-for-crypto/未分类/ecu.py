def ecu(l):
	a=l[0]
	b=l[1]
	x=[1,0,a]
	y=[0,1,b]
	while y[2]>0:
		q=x[2]/y[2]
		temp=[]
		for i in range(3):
			temp.append(x[i]-q*y[i])
		x=y
		y=temp
	return x

print ecu([657,963])