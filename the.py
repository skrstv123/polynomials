
class angle:
	"""for various operations with angles of the format degree.minute.second
	"""

	def __init__(self,d,m,s):
		self.degree=d
		self.minute=m
		self.second=s
	def ang(self):
		print("{0}°{1}'{2}\"".format(self.degree,self.minute,self.second))
	def todegree(self):
		y=round(self.degree+self.minute/60+self.second/3600,2)
		x=str(y)+"°"
	
		return x
	def addindeg(ax,ay):
		ax=angle.todegree(ax)
		ay=angle.todegree(ay)
		ax,ay=list(ax),list(ay)
		ax.remove("°")
		ay.remove("°")
		ax,ay=float("".join(ax)),float("".join(ay))
		return str(ax+ay)+"°"
	def addindms(ax,ay):
		s=(ax.second+ay.second)
		ss=round(s/60,2)
		sr=ss%60
		m=ax.minute+ay.minute+ss
		mm=round(m/60,2)
		mr=m%60
		deg=ax.degree+ay.degree+mm
		o=angle(deg,mr,sr)
		return o


"""a1=angle(24,2,10)
angle.ang(a1)
a1.ang()
print(angle.todegree(a1))
print(a1.todegree())
print(a1)
a2=angle(22,4,1)
print(angle.addindeg(a1,a2))
l=angle.addindms(a1,a2)
l.ang()
print(angle.todegree(l))"""


class poly:
	"""for multiplication & differentiation of polynomials 
	"""

	def __init__(self,c):
		self.coeff=c
		
	def reppoly(self):
		l=len(self.coeff)
		c=self.coeff
		pow=[x for x in range(l)]
		pow=pow[::-1]
		pstr=""
		for qw in range(l-1):
			pstr+=str(c[qw])+"x^"+str(pow[qw])+"+"
		pstr+=str(c[l-1])
		return pstr
	
	def polymul(fx,gx):
		f=fx.coeff[::-1]
		g=gx.coeff[::-1]
		re=[]
		df,dg=len(f),len(g)
		if df<dg:
			f,g=g,f
		dres,smth,smth2=df+dg-2,0,1
		if dres%2 not in [0]:
					smth+=1
		for p in range(dres+1):
			ts=0
			if p<=dres//2:
				smth+=1
				for q in range(p+1):
					ts+=f[q]*g[p-q]
			else:
				
				for q in range(smth2,smth):
					ts+=f[q]*g[p-q]
				smth2+=1
			
			re.append(ts)
		re=re[::-1]
		prod=poly(re)
		return (prod)
		"""
		coeff of kth term is given by 
		coeff(k)=sum{f[i]*g[k-i]} where i in [0,k+1] ->not sure about it though
		edit: the multiplication of coeffs follows a specific pattern & it can be easily understood from the definition itself , just go through the loops ☻
		resultant poly is of degree f+g 
		where, f=deg of fx 
		 g=deg of gx
		 algo author: skrstv123
	  """
		
	def diff(self,o): #first arg is the polynomial and next is the order of derivative you want
		c,p=self.coeff,len(self.coeff)
		for _ in range(o):
			x=[v for v in range(p-_)]
			x=x[::-1]
			for a in range(len(c)):
				c[a]*=x[a]
			c=c[:len(c)-1]
		return poly(c)
			
				
gx=poly([2,1])
fx=poly([4,2,1])
rx=(poly.polymul(gx,fx))

print('polynomial fx is:',poly.reppoly(fx),'\npolynomial gx is:',poly.reppoly(gx),'\npolynomial product of fx & gx is rx:',poly.reppoly(rx),'\nsecond order differential of polynomial rx is:',poly.reppoly(poly.diff(rx,2)))
#print(poly.__doc__)




















