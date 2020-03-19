n, k = map(int, input().split())
cont = 0
for i in range(0, n):
	cont = cont + 1 if (int(input()) % k) == 0 else cont
print(cont)
