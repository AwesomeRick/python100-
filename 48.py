string = input("输入")
long = len(string)-1
if string[0] == "(" and string[long] == ")":

        print("Ture")

elif string[0] == "[" and string[long] == "]":

        print("True")

elif string[0] == "{" and string[long] == "}":

        print("True")
else:
    print("False")