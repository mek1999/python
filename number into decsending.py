a=int(input())
b=[]
while a>0 :
	rem=int(a%10)
	b.append(rem)
	a=int(a/10)
b.sort(reverse=True)
print(b)
s = "".join(map(str, b)) 
print(s)
