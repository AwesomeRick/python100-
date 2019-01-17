a = [123,4,56,78,9,10,1]
b = []
m = 5
b += a[len(a)-m:len(a)]
b += a[0:len(a)-m]
print(b)