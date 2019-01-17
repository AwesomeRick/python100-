a = [2,1,3,4,5,6,7,9,8]
a[a.index(max(a))],a[0] = a[0],a[a.index(max(a))]
a[a.index(min(a))],a[len(a)-1] = a[len(a)-1],a[a.index(min(a))]
print(a)