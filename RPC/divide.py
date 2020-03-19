developers, dolars = map(int, input().split())
problems_solved = 0

list_cant_problems_by_developer = []
for i in range(developers):
    cant_solved = int(input())
    list_cant_problems_by_developer.insert(i,cant_solved)
    problems_solved += cant_solved

dolar_by_problem = dolars / problems_solved

for i in range(developers):
    print(int(list_cant_problems_by_developer[i]*dolar_by_problem))