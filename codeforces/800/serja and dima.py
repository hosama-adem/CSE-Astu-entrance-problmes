n = int(input())
a = list(map(int, input().split()))

l, r = 0, n - 1
s = d= 0
t = 0  

while l <= r:
    if a[l] >= a[r]:
        p = a[l]
        l += 1
    else:
        p = a[r]
        r -= 1

    if t == 0:
        s += p
        t = 1
    else:
        d += p
        t = 0

print(s, d)
