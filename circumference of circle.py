def circum(r) :
  	c=float(2*(22/7)*r)
	print("{:.2f}".format(c));
radi=int(input())
if radi<0 :
  	print("Error")
else :
	circum(radi)
