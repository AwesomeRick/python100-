L = []

for i in range(101,201):
    flag = 0
    for u in range(2,i):
        if i % u == 0:
            flag=1
            break
    if flag == 0:
        L.append(i)
print(L,"共有%d个素数" %len(L))