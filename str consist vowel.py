a=input()
count=0
for i in range(len(a)) :
	if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u' or a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U' :
		count+=1
		break
if count>=1 :
    print("yes")
else :
	print("no")	
