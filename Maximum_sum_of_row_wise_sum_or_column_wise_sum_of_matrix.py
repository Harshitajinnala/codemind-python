r,c = map(int,input().split())
m = []
for i in range(r):
    l = list(map(int,input().split()))
    m.append(l)
s = []
for i in m:
    x = sum(i)
    s.append(x)
print(max(s))