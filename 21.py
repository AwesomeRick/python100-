x = "abcd   12."#4字母，3空格，两数字，1字符
num, word, space,other = 0,0,0,0
for chr in x:
    if chr.isdigit():
        num += 1
    elif chr.isalpha():
        word += 1
    elif chr.isspace():
        space += 1
    else:
        other += 1
print("字母有%d，数字有%d,空格有%d,其他字符有%d" %(word,num,space,other))