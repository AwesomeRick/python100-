a,b,s = 2,1,0
for i in range(21):
    s = s+a/b
    a, b = a+b, a
print(s)