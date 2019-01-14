for i in range(100,1000):
    num1 = i%10
    num2 = i//10%10
    num3 = i//100%10
    if num1**3+num2**3+num3**3==i:
        print(i)