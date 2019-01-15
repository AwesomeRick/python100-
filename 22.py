n = int(input("输入数字的个数"))
# 假设数字为2
m, s = "", 0
for i in range(1,n+1):
     m = m + "2"
     s = s + eval(m)
print(s)