def inv(small,mod):
    "x*mod+y*small=gcd(small,mod)"
    x=[1,0]
    y=[0,1]
    r=[mod,small]
    while r[1]>0:
        q=r[0]/r[1]
        temp=x[1]
        x[1]=x[0]-q*x[1]
        x[0]=temp
        
        temp=y[1]
        y[1]=y[0]-q*y[1]
        y[0]=temp
        
        temp=r[1]
        r[1]=r[0]%r[1]
        r[0]=temp

    return [y[0],x[0],r[0]]

def add(p,q,a,mod):
    if p!=q:
        temp=(q[1]-p[1])%mod
        k=temp*inv(q[0]-p[0],mod)[0]%mod
    else:
        temp=(3*(p[0]**2)+a)%mod
        k=temp*inv(2*p[1],mod)[0]%mod
    x=(k**2-p[0]-q[0])%mod
    y=(k*(p[0]-x)-p[1])%mod
    return [x,y]

def main():
    a=2
    b=17
    mod=31
    p=[10,13]
    r=p
    key=20
    for i in xrange(key):
        r=add(p,r,a,mod)
        print i,r
    

if __name__ == '__main__':
    main()