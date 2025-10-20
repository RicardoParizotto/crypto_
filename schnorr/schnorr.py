#!/usr/bin/env sage
from sage.all import *
import random


# 1) Parameters
q = 1000
#G = Integers(q)  #this should be a cyclic group used to generate g

R = Integers(q) 

g = R.random_element()

print(g)

# 2) Key Gen
#secret key
a = R.random_element()
print("secret s:", a)

#public key
u = g**a

#Verifier BOB
#challenge
#this is the challenge space
C = random.sample(R.list(), 9)
print(C)
c = random.choice(C)  

#Prover Alice
at = R.random_element()
ut = g**at    #this is the commitment

az = at + a*c


if g**az == ut*(u**c):
   dec = 1
else:
   dec = 0

print("decrypted:", dec)
print("correct?", dec == 1)


