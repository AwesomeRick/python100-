count = 0
for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            if (x != y) & (x !=z)  & (y != z):
                print("%d%d%d" % (x, y, z), end='  ')
                count += 1
    print('')
print('最终结果为：%s个' % count)
