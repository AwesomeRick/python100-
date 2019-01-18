Mingwen = 5896
t = 0
for i in range(4):
    s = Mingwen % 10
    Mingwen = Mingwen//10
    s = (s+5) % 10
    t = t + s * 1000/(10**i)
print(t)