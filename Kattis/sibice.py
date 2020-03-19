import math
cant_cases,w,h=map(int,input().split())
for i in range(cant_cases):
    n=int(input())
    if n<=h or n<=math.sqrt((w**2)+(h**2)):
        print("DA")
    else:
        print("NE")
