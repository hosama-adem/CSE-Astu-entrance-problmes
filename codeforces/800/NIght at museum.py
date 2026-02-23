s = input()
c = 'a'
mo = 0
for i in s:
  diff = abs(ord(i) - ord(c))
  mo += min(diff, 26 - diff)
  c = i
print(mo)
