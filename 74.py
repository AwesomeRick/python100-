for i in range(1,5000):
    t = i
    m = 0
    for n in range(1,6):
        if (i-1)*4/5%1 !=0:
            m = 1
            break
        i=(i-1)*4/5
    if m == 0:
        print(t)