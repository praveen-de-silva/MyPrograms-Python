# =======================
# PROGRAM : Number System
# =======================

num = 0.25
base = 2
conv = []

def convert():
    pass

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

##conv.reverse()
##numConv = ''.join(conv)   
##print(numConv)


def findFloat(num):
    fPart = ''
    tempFloat = num%1

    for _ in range(10):
        if tempFloat==0:
            fPart += '0'
            return float(f'0.{fPart}')

        tempMul = tempFloat * base

        if int(tempMul)==1:
            fPart += '1'
        else:
            fPart += '0'

        tempFloat = tempMul%1
    return int(f'0.{fPart}')

a = findFloat(0.625)
print(a)  
    
