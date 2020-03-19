def nCk(n,k) : 
    return (fact(n) / (fact(k)* fact(n - k))) 
def fact(n) : 
    res = 1
    for i in range(2, n+1) : 
        res = res * i 
    return res 
l= list(map(int,input().split(" ")))
n=l[0]
k=l[1]
print(int(nCk(n, k))) 
  
