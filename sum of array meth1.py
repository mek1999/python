#sum of array with list method 1
n=int(input())
arr = list(map(int,input().split(" ")))
a=arr[:n]
s=sum(a)
print(s)
