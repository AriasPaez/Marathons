cases = int(input())
for i in range(cases):
    input()
    Mg ,Mm = map(int,input().split())
    Lg = input().split()
    Lm = input().split()
    while len(Lg) > 0 and len(Lm) > 0:
        minLg=min(Lg)
        minLm = min(Lm)

        if minLg==minLm:
            Lm.remove(minLm)
        elif minLm>minLg:
            Lg.remove(minLg)
        elif minLg>minLm:
            Lm.remove(minLm)

    if len(Lg) == 0 and len(Lm) == 0:
        print("uncertain")
    else:
        if len(Lg)== 0:
            print("MechaGodzilla")
        elif len(Lm)== 0:
            print("Godzilla")

    if Mg == 0 and Mm == 0:
        print("uncertain")




# print("cases:",cases)
# print("Mg:",Mg," Mm:",Mm)
# print("Lg: ",Lg)
# print("Lm: ",Lm)