#每个月的兔子总数符合斐波那契数列乘二
n = int(input("第几个月"))
a,b=1,1
for i in range(0,n-2):
    a,b=b,a+b
print("这个月共有%d个兔子" %(2*b))