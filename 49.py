n = input("输入")
l = len(n)-1
if n[0] == "(" and n[l] == ")":
    print("True")
elif n[0] == "[" and n[l] == "]":
    print("True")
elif n[0] == "{" and n[l] == "}":
    print("True")
else:
    print("False")