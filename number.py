#gcd(a,b) tra ve uoc chung lon nhat
#a > b
#a = b. q + r
def gcd1(a,b):
    r = a % b
    if r == 0:
        return b
    else:
        return gcd1(b, r)
def lcm(a,b):
    h = gcd1(a,b)
    i, j = a / h , b/h
    return h * i *j
def sumdivisor(n):
    s = 0
    h = n //2
    for i in range(1,h + 1):
        if n % i ==0:
            s += i
    return s + n

            
