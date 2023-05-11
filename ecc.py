from addition import addition, repeated_addition

def inverse(P,p):
    return (P[0],(-1*P[1])%p)

def encrypt(message,G,key_S,key_R,a,b,p):
    int_size=len(bin(p))-2
    cipher_text=""
    start=0
    while(start<len(message)):
        s=message[start:start+8]
        m=int(s,2)
        M=(m,pow(((pow(m,3,p)+(a*m)%p+b)%p),(p+1)//4,p))
        c=addition(M, repeated_addition(key_S[0], key_R, a, b, p), a, b, p)
        x=(int_size-len(bin(c[0])[2:]))*"0"+bin(c[0])[2:]
        y=(int_size-len(bin(c[1])[2:]))*"0"+bin(c[1])[2:]
        cipher_text+=x
        cipher_text+=y
        start+=8
    return cipher_text

def decrypt(cipher_text,G,key_S,key_R,a,b,p):
    message=""
    int_size=len(bin(p))-2
    start=0
    while(start<len(cipher_text)):
        c=cipher_text[start:start+2*int_size]
        C=(int(c[:int_size],2),int(c[int_size:],2))
        m=addition(C, inverse(repeated_addition(key_R[0], key_S, a, b, p),p), a, b, p)
        M=(8-len(bin(m[0])[2:]))*"0"+bin(m[0])[2:]
        message+=M
        start+=2*int_size
    return message