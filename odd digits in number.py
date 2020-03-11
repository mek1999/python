s=(input())
res = list(map(int, str(s)))
count=0
for i in range(len(res)) :
  if res[i]%2!=0 :
    print(res[i],end=" ")
    count+=1
  else :
    continue
if count<1 :
  print("-1")
