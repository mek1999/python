li= list(map(int,input().split(' ')))
a=li[0]
b=li[1]
c=li[2]
if (a+b > c and a+c > b and b+c > a) :
	print("yes")
else :
  	print("no")
