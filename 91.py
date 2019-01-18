d = {'a': 2, 'b': 1, 'c': 8, 'd': 5}
L = sorted(d.values())
b = {}
for x,y in zip(d.keys(),L):
    b[x] = y
print(b)