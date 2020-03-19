n1, n2 =map(str,input().split())
n1=n1[::-1]# STRING AL REVES

n2=n2[::-1]
if int(n1)>int(n2):
    print(n1)
else:
    print(n2)