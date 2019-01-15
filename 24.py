high = 100
s = 0
for i in range(0,10):
    s = s + high
    high *= 1/2
print("路程%.2f m,第10次反弹%.2f m" %(s,high))