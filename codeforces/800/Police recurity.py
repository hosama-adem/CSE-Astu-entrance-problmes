n = int(input())  
a = list(map(int, input().split()))  

o = 0  
u = 0  

for e in a:
    if e == -1:
        if o > 0:
            o -= 1
        else:
            u += 1
    else:
        o += e  

print(u)
