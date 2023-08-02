n=int(input())
l=list(map(int,input().split()))
x = n//2
s=[]
p=[]
for i in range(0,x):
   s.append(l[i])
for i in range (n//2,n):
   p.append(l[i])
p.reverse()
p.extend(s)
print(*p)