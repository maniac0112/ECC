import math

def mod_inverse_general(x,n):
    for i in range(1,n):
        if (((x % n) * (i % n)) % n == 1):
            return i
    return -1

def mod_inv(x,p):
    g = math.gcd(x,p)
    if (g != 1):
        return mod_inverse_general(x,p)
    else:
        return pow(x,p-2,p)