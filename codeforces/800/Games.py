#hos
n = int(input())  
a = []
for _ in range(n): 
    team = tuple(map(int,input().split()))
    a.append(team)

count = 0
for i in range(n):
    for j in range(n):
        if i != j and a[i][0] == a[j][1]:
            count += 1

print(count)
