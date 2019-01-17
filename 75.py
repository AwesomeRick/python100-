a ="asdfghjkla"
t = 0
for i in a:
    if a.count(i) == 1:
        print(a.find(i))
        t = 1
        break
if t == 0:
    print(-1)