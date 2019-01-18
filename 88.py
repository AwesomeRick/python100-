a = "zxcvbnm"
b = "zxcvuiiiiip"
l = 0
if len(a)<=len(b):
    for i in range(len(a)):
        for o in range(i,len(a)):
            if a[i:o] in b and o-i>l:
                l = o - i
print(l) 