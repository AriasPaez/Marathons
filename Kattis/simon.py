cant_cases= int(input())
for i in range(cant_cases):
    line=input()
    if (line.upper().find("simon says ")==0):
        print(line.upper().replace("simon says ",""))