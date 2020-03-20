st=input()
s=len(st)
count=0
for i in range(s) :
  for j in range(i) :
    if st[i]==st[j] :
      count+=1
if count>=2 :
  print(count)
else :
  print("-1")
