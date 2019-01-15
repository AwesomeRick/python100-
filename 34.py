def reverse(ch,n):
    if n == 0:
        return ch[0]
    return print(ch[n-1],end=""),reverse(ch,n-1)


n = 12345
m = str(n)
t = 0
while n != 0:
    n = n//10
    t += 1
reverse(m,t)
print('\n%s是%d位数' %(m,t))