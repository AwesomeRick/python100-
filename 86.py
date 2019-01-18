L = []
f = open("C:/Users/AwesomeRick/Desktop/A.txt", "r")
a = f.read()
f.close()
r = open("C:/Users/AwesomeRick/Desktop/B.txt", "r")
b = r.read()
r.close()
c = a + b
d = ""
for i in c:
    L.append(i)
L.sort()
for i in L:
    i = str(i)
    d = d + i
p = open("C:/Users/AwesomeRick/Desktop/C.txt", "w")
p.write(d)
p.close()