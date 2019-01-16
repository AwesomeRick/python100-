a = 123456789
for i in range(7):
    if i == 0:
        s = a % 10
    else:
        a = a//10
        s = a % 10
    print(s,"  ")