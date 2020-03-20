n=int(input())
arr = list(map(int,input().split(" ")))
a=arr[:n]
a.reverse()
print(a)
s = "->".join(map(str,a)) 
print(s)
