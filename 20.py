a, b = "Fizz", "Buzz"
n = int(input("输入n"))
c=""
for i in range(1,n+1):
    x = ""
    if i%3 == 0:
        x = x+a
    if i%5 == 0:
        x = x+b

    print(i,x)
    c = c+str(i)
print(c)