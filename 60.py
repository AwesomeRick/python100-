a = -12345678123456781234567812345678
s = "-"
if a < 0:
    a = str(a)
    for i in range(32):
        s = s + a[32-i]
    print(s)
else:
    a = str(a)
    for i in range(32):
        s = s + a[31-i]
    print(s)
