import math
k, x = map(int, input().split())
m = max(k, x)
f = 6 - m + 1
t = 6
g = math.gcd(f, t)
print(f"{f//g}/{t//g}")
