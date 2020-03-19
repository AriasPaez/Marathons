megas=int(input())
cases=int(input())
aux_mega=megas
for i in range(cases):
    N=int(input())
    aux_mega=aux_mega-N+megas
print(aux_mega)
