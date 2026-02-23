#hos
n = int(input())
a = list(map(int,input().split()))
t = int(input())
for _ in range(t):
    x,y = list(map(int,input().split()))
    x -= 1

    l = y-1
    r = a[x] - y

    if x > 0:
        a[x-1] += l

    if x < n - 1:
        a[x+1] += r
    
    a[x] = 0

for i in a:
    print(i)
