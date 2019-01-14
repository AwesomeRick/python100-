l=[1,1]
a,b=1,1
n=int(input("你想要多少位斐波那契数列？\n(至少一位)\n"))
for i in range(0,n):
    a,b=b,a+b
    l.append(b)
print(l[0:n])