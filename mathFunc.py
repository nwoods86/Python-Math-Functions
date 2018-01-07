##Math Functions


#Function Definitions
def fac(n):             #calculates the factorial of input N, if negative number is entered than the positive
    res = 1             #result is returned.
    num = 1
    if (n < 0):
        n *= -1
    while(num <= n):
        res = num * res
        num +=1
    return(res)

def cos(rad): #Calculates cosine for the Value passed in.
    count = 0
    res = 0
    while(count < 25):
        t1 = (-1)**count
        t2 = 2*count
        t3 = fac(t2)
        t4 = rad**t2
        t5 = t1/t3
        t6 = t5 * t4
        res += t6
        count += 1
    return(res)

def sin(rad):   #calculates sine using the cos() function. (Use radians)
    pi = 3.14159265358979323846264338327950288419
    res = cos(rad + (pi/2))
    return(-res)

def tan(rad):   #calculates tangent using the cos() and sin() functions. (Use radians)
    sinX= sin(rad)
    cosX = cos(rad)
    res = sinX/cosX
    return(res)

def sqrt(num):  #calculates the sqaure root of the inputed number. (Use radians)
    return(num**(1/2))


def ln(number): #calculates the natural log of the inputed number. Has 11 digits of accuracy.
    n = 0
    res = 0
    while(n<1000):
        t1 = (2*n) + 1
        t2 = 1/t1
        t3 = number - 1
        t4 = number + 1
        t5 = t3/t4
        t6 = t5**t1
        t7 = t2*t6
        res += t7
        n += 1
    res2 = 2*res
    resf = round(res2, 11)
    return(resf)

def log(number, base): #uses the ln() function to calculate the log of the input
    t1 = ln(number)
    t2 = ln(base)
    res = t1/t2
    return(res)


rad = eval(input("what is your angle (in Radians)?"))   #gets an input from the usr
print(log(8, 2))                                     #prints the result to the screen




