i=2
for n in range(1,10):
    for m in range(1,i):
        print("%d * %d = %d" %(m,n,m*n),end="  |  ")
    print("\n")
    i+=1