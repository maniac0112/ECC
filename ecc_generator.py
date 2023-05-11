import math
import prime_generator
import random
from addition import addition,repeated_addition
from ecc import encrypt, decrypt, inverse


#let the elliptic curve be -

def ecc_generator(prime_bits):
    p=prime_generator.generate_prime(prime_bits)
    for j in range(prime_bits,prime_bits+5):
        count=0
        while ((p+1)%4!=0 and count<50):
            p=prime_generator.generate_prime(j)
            count+=1
        #this ensures all the elements have a square root in the prime field!

    a=random.randrange(2**(prime_bits-2)-1,2**(prime_bits-1)-1)
    b=random.randrange(2**(prime_bits-2)-1,2**(prime_bits-1)-1)
    while(a==b or (4*pow(a,3,p)+27*pow(b,2,p))%p==0):
        a=random.randrange(2**(prime_bits-2)-1,2**(prime_bits-1)-1)
        b=random.randrange(2**(prime_bits-2)-1,2**(prime_bits-1)-1)

    #now that we have chosen appropriate p,a,b 
    #we not choose a good base point!
    #we would want that it has a high order ~ >10,000 for this example!

    x=random.randrange(2**(prime_bits-2)-1,2**(prime_bits-1)-1)
    y=pow(((pow(x,3,p)+(a*x)%p+b)%p),(p+1)//4,p)
    while(1):
        order=0
        point=(x,y)
        while(point!="O"):
            order+=1
            point=addition(point, (x,y), a, b, p)
        if order>10000:
            break
        x=random.randrange(1,22)
        y=pow(((pow(x,3,p)+(a*x)%p+b)%p),(p+1)//4,p)

    G=(x,y)
    return (a,b,p,G)
