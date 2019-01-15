s1 = input("输入第一个字母")
if s1 == "M":
    print("Monday")
elif s1 == "T":
    s2 = input("输入第二个字母")
    if s2 == "u":
        print("Tuesday")
    elif s2 =="h":
        print("Thursday")
elif s1 == "W":
    print("Wednesday")
elif s1 == "S":
    s2 = input("输入第二个字母")
    if s2 == "u":
        print("Sunday")
    elif s2 == "a":
        print("Saturday")
else:
    print("请输入正确的首字母或第二个字母")