i=int(input("输入利润  单位万元"))
if i<= 10:
    w=i*0.1
elif i<=20:
    w=(i-10)*0.075+1
elif i<=40:
    w=(i-20)*0.005+1.75
elif i<=60:
    w=(i-40)*0.03+2.75
elif i<=100:
    w=(i-60)*0.015+3.35
else:
    w=(i-100)*0.01+3.95
print("奖金为%d元" %(w*10000))