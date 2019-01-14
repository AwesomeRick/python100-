import math

for s in range(-99,10000):
    t=math.sqrt(s + 100)% 1
    m=math.sqrt(s + 168+100)% 1
    if t==0 and m==0:
        print(s)