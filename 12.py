n = int(input("输入一个整数"))
thr = 1
while thr <= n:
    if thr < n:
        thr *= 3
    else:
        print("是三的幂次方")
        break
if thr > n:
    print("不是三的幂次方")
