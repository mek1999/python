#sum of array with list method 2
total = 0 
n=int(input())
arr = list(map(int,input().split(" ")))
a=arr[:n]
for ele in range(0, len(a)): 
    total = total + a[ele] 
print(total)
