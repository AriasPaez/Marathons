n=int(input())
for i in range(n):
    N=int(input())
    if N==0 or N==1:
        print(1)
    elif N>=5:
        print(0)

    else:
        fact=1
        for j in range(1,(N+1)):
            fact *=j

        print(str(fact)[len(str(fact))-1:])

