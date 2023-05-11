from inverse_mod import mod_inv

def addition(P,Q,a,b,p):
    if P=="O":
        return Q
    elif (Q=="O"):
        return P
    elif P==Q:
        if P[1]==0:
            return "O"
        m=((mod_inv((2*P[1])%p, p))*(((3*(pow(P[0],2,p))%p)+a)%p)%p)%p
        x=((m*m)%p-(P[0]+Q[0])%p)%p
        y=((m*((P[0]-x)%p))%p-P[1])%p
        return (x,y)
    else:
        if P[0]==Q[0] and P[1]==-Q[1]%p:
            return "O"
        m=(mod_inv((P[0]-Q[0])%p, p)*((P[1]-Q[1])%p))%p
        x=((m*m)%p-(P[0]+Q[0])%p)%p
        y=((m*((P[0]-x)%p))%p-P[1])%p
        return (x,y)


def repeated_addition(k,G,a,b,p):
    arr=[]
    start=1
    while(1):
        if start==1:
            arr.append(G)
        else:
            arr.append(addition(arr[-1], arr[-1], a, b, p))
        if 2**start-1>=k:
            break
        start+=1
    arr.reverse()
    x=bin(k)[2:]
    point="O"
    for i in range(len(x)):
        if x[i]=="1":
            point=addition(point, arr[i], a, b, p)
    return point