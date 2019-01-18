def climb(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return climb(n-1)+climb(n-2)
print(climb(4))
