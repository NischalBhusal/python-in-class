d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 2, 'b': 3, 'd':4 }
for k,v in d1.items():
    if k in d2:
        print(k, v, d2[k])
    else:
        print(k, v, 'not found in d2') 