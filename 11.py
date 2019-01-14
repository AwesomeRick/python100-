x=int(input("请输入一个无符号整数"))
a=bin(x)
count=0
m="ddd"
for num in str(a)[2:len(str(a))]:
    if num=="1":
       count+=1
print("它的二进制为%s"%str(a)[2:len(str(a))])
print(count)