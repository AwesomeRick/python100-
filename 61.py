a = int(input("输入第一个"))
b = int(input("输入第二个"))
c = int(input("输入第三个"))
m = max(a,b,c)
n = min(a,b,c)

print("最大的：",m)
if a<m and a>n:
    print(a)
elif b<m and b>n:
    print(b)
elif c<m and c>n:
    print(c)
print("最小的：",n)