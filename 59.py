
def oval(start,end,a,flag):
    import turtle
    if flag == 1:
        for i in range(start, end):
            turtle.fd(a)
            turtle.left(90 / (end - start))
            a = a + 0.3
    if flag == -1:
        for i in range(start, end):
            turtle.fd(a)
            turtle.left(90 / (end - start))
            a = 0.3 -a



for i in range(2):
    s,a =0,0
    oval(s,s+30,a,1)
    oval(s,s+30,a,-1)
