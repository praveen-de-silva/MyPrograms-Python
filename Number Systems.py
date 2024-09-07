num = 1234
base = 16
conv = []

quo = num

while True:
    rem = quo%base

    if rem<10:
        conv += str(rem)
    elif 10<=rem<36:
        conv += chr(64 + rem - 9)
    else:
        conv += [f"({str(rem)})"]
    
    quo //= base

    if quo==0:
        break

conv.reverse()
numConv = ''.join(conv)   
print(numConv)

