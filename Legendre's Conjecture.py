def isPrime(num):
    '''check num is prime'''
    if num in [0, 1]:
        return False

    for div in range(2, int(num**0.5)+1):
        if num%div==0:
            return False

    return True

def getPrimes(num):
    '''find the primes between the range'''
    primes = []
    
    for i in range(num**2+1, (num+1)**2):
        if isPrime(i):
            primes.append(i) # collecting primes

    return primes

def setStatement(num, primes_arr):
    '''make the True statement'''
    # Line 02 :
    primes_str = [str(x) for x in primes_arr] # arr of strings of primes
    primes_str_line = ', '.join(primes_str) # comma seperated line containing all primes 
    line2 = f"primes between {num}^2 and ({num}+1)^2 : {primes_str_line}"

    # Line 01 :
    gap = line2.index(':')
    line1_left = "State for n = " + str(num)
    line1 = f"{line1_left.ljust(gap, ' ')}: TRUE" # to vertically align ':' 
    
    return line1 + '\n' + line2

def LegendreConjecture(num):
    primes = getPrimes(num)

    if len(primes)==0: # False case
        print(f"State of conjecture for n = {num} : FALSE")
        return

    statement = setStatement(num, primes) # True case
    print(statement)

LegendreConjecture(10)
