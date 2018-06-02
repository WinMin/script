def sheng():
	r=int(raw_input("input len: "))
	a=[0 for i in xrange(r)]
	m=[0 for i in xrange(r)]
	for i in xrange(r):
		a[i]=int(raw_input("input a%d: "%i))
		m[i]=int(raw_input("input m%d: "%i))
	temp=1
	for i in xrange(r):
		temp*=m[i]
	M=[0 for i in xrange(r)]
	for i in xrange(r):
		M[i]=temp/m[i]
	y=[0 for i in xrange(r)]
	for i in xrange(r):
		y[i]=ecu(M[i],m[i])
	final=0
	for i in xrange(r):
		final+=a[i]*M[i]*y[i]%temp
	return final

def ecu(b,a):
	a0=a
	t0=0
	t=1

	q=a/b

	r=a-q*b

	while r>0:
		temp=(t0-q*t)%a0
		t0=t
		t=temp
		a=b
		b=r
		q=a/b
		r=a-q*b

	return t

if __name__ == '__main__':
	print sheng()
