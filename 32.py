def reverse(ch,n):
    if n == 0:
        return ch[0]
    return print(ch[n-1],end=""),reverse(ch,n-1)
reverse(input("输入五个字符"),5)