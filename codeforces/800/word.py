#hos
t = input()
up = 0
for i in t:
    if i == i.upper():
        up += 1

if len(t)//2 < up:
    print(t.upper())
else:
    print(t.lower())
