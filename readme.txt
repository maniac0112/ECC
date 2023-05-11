"""This is a brief outline of what each of the files does

main.py => It is made for demostrating the entire working of this elliptic curve cryptography. 

First, it converts an image into a binary sequence. This binary sequence is then encrypted using ECC.

The file ecc_generator, generates an elliptic curve on a prime field of specified size. It gives a and b for the elliptic
curve, such that it is non-singular. It also generates a base point G, which has a high order.

The ecc file contains two functions encrypt and decrypt, which takes in curve parameters, prime, base point
sender keys, reciver's public key and message as input and gives the output. The decrypt takes all of this too with
the exception of ciphertext instead of message, but it takes only public key of sender and both 
public and private key of reciver.

The main function uses these two files to generate first generate an elliptic curve. Then using senders key and 
receiver key, encrypts the binary sequence to ciphertext and saves it. Later it decrypts the same, and transform the 
decrypted sequence back into an image named decrypted.jpg.

The addition file contains code for adding two points on the curve. The repeated addition in the same file 
performs kG (repeated addition) in O(log(k)) time

The inverse mod computes the inverse modulo p of a number, which is heavily used in addition of points.

The prime generator generates prime number of desired size (in bits) and is used by ecc_generator

"""