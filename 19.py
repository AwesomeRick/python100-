a = 0b10101010101010101010101010101010
a = str(bin(a))
b = "0b"
for ch in a[1:len(a)+1]:
    if ch == "1":
        b = b+"0"
    else:
        b = b+"1"
print(b)