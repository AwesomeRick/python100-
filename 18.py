import time
print(time.asctime(time.localtime(time.time())))#最易读的方式
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))#可以自已定义时间的格式