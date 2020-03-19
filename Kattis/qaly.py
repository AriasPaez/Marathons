n=int(input())
avac=0
for i in range(n):
    a,b=map(float,input().split())
    avac +=a*b

print(avac)