L1 = [1,94,3,5,58,4,13]
L2 = [1,3,4,99,999,58]
L = []
for i in L1:
    if i in L2:
        L.append(i)
print(L)