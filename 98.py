import random
for i in range(4):
    t = random.randint(0,1)
    if t == 1:
        t = random.randint(65, 90)
        t = chr(t)
    elif t == 0:
        t = random.randint(0, 9)
    print(t,end="")