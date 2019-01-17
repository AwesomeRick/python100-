def mmm(n):
    if n%2 == 0:
        s = 0
        for i in range(2,n+1,2):
            s += 1/i
        return print(s)
    if n%2 == 1:
        s = 0
        for i in range(1,n+1,2):
            s += 1/i
        return print(s)
mmm(9)