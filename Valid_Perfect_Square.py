import math
n=int(input())
for i in range(n):
    x=int(input())
    a=int(math.sqrt(x))
    if (a*a==x):
        print("True")
    else:
        print("False")