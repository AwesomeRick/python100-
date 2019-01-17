L = ["xyz","xzy","yxz","yzx","zyx","zxy"]
for a,b,c in L:
    if a != b and b != c and a != c and a != "x" and c != "x" and c != "z":
        print("abc分别对阵",a,b,c)