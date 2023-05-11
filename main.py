import cv2
import numpy as np 
import os
import matplotlib
import sys

from ecc_generator import ecc_generator
from ecc import encrypt, decrypt
from addition import repeated_addition, addition


def convert(s):
    arr=s.flatten()
    output=""
    for i in range(arr.shape[0]):
        t="0"*(8-len(bin(arr[i]))+2)+bin(arr[i])[2:]
        output+=t
    return output
        
def retrieve(arr,shape):
    output=[]
    for i in range(shape[0]):
        output.append([])
        for j in range(0,shape[1]):
            rgb=arr[(i)*shape[1]*24+j*24:(i)*shape[1]*24+j*24+24]
            r=int(rgb[0:8],2)
            g=int(rgb[8:16],2)
            b=int(rgb[16:24],2)
            z=[r,g,b]
            output[i].append(z)
    op=np.array(output)
    return op

def main(image):

    print("Please Wait...")
    print("It may take some time")

    s=cv2.imread(image)
    shape=s.shape
    x=convert(s)
    t=len(x)


    params=ecc_generator(16) #[a,b,p,G]
    sender_key=[21,repeated_addition(21,params[3],params[0],params[1],params[2])] #[private key, public key]
    receiver_key=[11,repeated_addition(11,params[3],params[0],params[1],params[2])] #[private key, public key]

    while(len(x)%8!=0):
        x+="0"

    ciphertext=encrypt(x, params[3], sender_key, receiver_key[1], params[0], params[1], params[2]) #ecc encryption

    #simply writing ciphertext in a txt file    
    f=open("ciphertext.txt","w")
    f.write(ciphertext)
    f.close()

    #now we decrypt the ciphertext!
    message=decrypt(ciphertext, params[3], sender_key[1], receiver_key, params[0], params[1], params[2])    
    decrypted=message[:t]
    z=retrieve(decrypted, shape)
    cv2.imwrite('decrypted.jpg',z)  

main("sample.jpg")
