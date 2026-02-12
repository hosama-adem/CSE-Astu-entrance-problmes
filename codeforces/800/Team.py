#hos
t = int(input())
count = 0

for _ in range(t):
    n,x,t = map(int,input().split())
    d = n+x+t
    if d >= 2:
        count +=1

print(count)
