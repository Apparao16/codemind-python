a = int(input())
def p(a):
	b= 0
	for i in range (2,int(a**0.5+1)) :
		if a % i == 0 :
			b +=1
	return(b<1and a != 1 )
b = list(filter(p,range(1,a+1))) 
b = [ (i,int(a/i) )for i in b if a/i in b]
if b == [] :
	print(-1)
else :
	print (*b[0])