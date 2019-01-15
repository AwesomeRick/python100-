# python没有数组，我就把它当成全是数的列表了
L = [35,1532165,1,54,6,13,1,321,31,5,4684,68,48,8,65,51,3,1]
flag = 0
for num in L:
    if L.count(num)>1:
        print("False")
        flag = 1
        break
if flag == 0:
    print("True")