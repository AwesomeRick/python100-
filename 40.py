s = int(input("输入一个数"))
for i in range(2,s):
    flag = 0
    for n in range(2,i):
        if i%n == 0:
            flag = 1
            break
    if flag ==0:
        print(i)