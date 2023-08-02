a = int(input())
b = int(input())
for i in range(a,b+1):
    c = 0
    z = str(i)
    for s in str(i):
        if int(s)!=0:
            if i % int(s) == 0:
                c+=1
    if len(z) == c:
        print(i,end =' ')