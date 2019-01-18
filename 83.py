m = "d"
t = ""
while m != "#":
    f = open("C:/Users/AwesomeRick/Desktop/P.txt","w")
    m = input("输入一个字符")
    t = t + m
    f.write(t)
    f.close()
