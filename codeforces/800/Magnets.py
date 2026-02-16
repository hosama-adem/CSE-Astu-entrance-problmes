#hos
t = int(input())
al = ""
c = 0
for _ in range(t):
    n = input()
    if n!=al:
        c += 1
        al = n
print(c)   
