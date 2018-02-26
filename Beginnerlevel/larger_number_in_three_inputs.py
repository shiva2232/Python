#python2 document
try :
	x=int(input("Enter three integer : "))
	y=int(input())
	z=int(input())
	def large(x,y,z):
		if x>y and x>z :
			return x
		elif y>x and y>z :
			return y
		else :
			return z
	n=large(x,y,z)
	print n
except :
	print "err..."
