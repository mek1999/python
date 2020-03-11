s=input()
i=len(s)
if i%2==0 :
  l=i//2
  s= s[:l-1]+"*"+s[l:]
  s= s[:l]+"*"+s[l+1:]
else :
  l=i//2
  s= s[:l]+"*"+s[l+1:]
print(s)
