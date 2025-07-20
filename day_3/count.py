s = input ("Enter a string: ")
d = {}
for i in s:
    if i not in d.keys():
        d[i] = s.count(i)
print(d)

