a = int(input())
def p(a):
	b= 0
	for i in range (2,int(a**0.5+1)) :
		if a % i == 0 :
			b +=1
	return(b<1and a != 1 )

t = a
k = 0
if p(a) == True :
	while a >0 :
		b =a%10
		if p(b)== False :
			print('Not Mega Prime')
			break
		a//=10
		k+=1
else :
	print ('Not Mega Prime')
if len(str(t)) == k :
	print('Mega Prime')