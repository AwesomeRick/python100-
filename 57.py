# 这是加入实验室以前做的，中心思路是把杨辉三角的每一行两侧都加上0，但是读取的时候不读取0
def Yanghui(max):
    n = 1
    a = []
    i = [0, 1, 0]
    while n < max:
        length = len(i)-1
        yield i[1:length]
        for s in range(1,length+1):
            b = i[s-1]+i[s]
            a.append(b)
        a.insert(0, 0)
        a.insert(len(a), 0)
        i = a
        a = []

o = Yanghui(8)
for t in range(1,8):
    print(next(o))