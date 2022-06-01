x = int(input())
def palin(a):
		b = str(a)[::-1]
		return b == str(a)
b = list(filter(palin,range(x)))
d = x
k = []
for i in b :
			c = abs(i -x)
			if c<d and c!=0:
				k = i
				d = c
				k =[i]
			elif c==d and c!=0:
				k.append(i)		
print(*k)