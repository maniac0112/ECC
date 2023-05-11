import random

primes= []

def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)
        
SieveOfEratosthenes(100)

def nBitRandom(n):
    return random.randrange(2**(n-1)+1, 2**n - 1)

def generate_prime(k):
    redo=False
    while(1):
        x=nBitRandom(k)
        if x%2==0:
            if len(str(x+1))>k:
                x-=1
            else:
                x+=1
        #check if this number has a divisor in <100
        for i in primes:
            if i>=x:
                break
            if x%i==0:
                redo=True
                break
        if redo:
            redo=False
            continue
        #passed the primary test
        #find the value of d
        curr=x-1 #this would be an even number
        e=0
        while(curr%2==0):
            e+=1
            curr=curr//2
        d=curr
        # n-1= 2^e*d 
        D={} #this will store non-witnesses for the miller rabin theorem
        for i in range(30):
            t=random.randint(2,200)
            while(t in D):
                t=random.randint(2,200)
            D[t]=1
            #now, our base is s!
            miller_seq=None
            witness=True
            for i in range(e):
                if i==0:
                    u=pow(t,d,x)
                    if u==1:
                        witness=False
                        break
                    miller_seq=u
                else:
                    u=pow(miller_seq, 2,x)
                    if u==x-1:
                        witness=False
                        break
                    miller_seq=u
            if witness:
                redo=True
                break
        if redo:
            redo=False
            continue
        return x