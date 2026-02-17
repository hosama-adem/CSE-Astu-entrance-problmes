#hos
a1,a2,a3,a4 = map(int,input().split())
t = input()
c = 0
for i in t:
    if i == "1":
        c += a1
    elif i == "2":
        c += a2
    elif i == "3":
        c += a3
    elif i == "4":
        c += a4

print (c)
