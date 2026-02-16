#hos
t = int(input())
n = input()
count = 0
for i in range(t-1):
    if n[i] == n[i+1]:
        count += 1

print(count)
