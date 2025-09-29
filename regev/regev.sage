#!/usr/bin/env sage
from sage.misc.prandom import randrange
import sage.stats.distributions.discrete_gaussian_integer as dgi

# 1) Parameters
q, n, m = 9, 4, 4
R = Integers(q)
Q = Rationals()
Z2 = Integers(2)

# 2) Helper function for noise
def sample_noise(N):
    D = dgi.DiscreteGaussianDistributionIntegerSampler(sigma=1.0)
    return vector([R(D()) for _ in range(N)])

# 3) Key Generation
# Secret key s (vector of length n)
s_vec = vector([R.random_element() for _ in range(n)])
print("secret s (vector):", s_vec)

# Public matrix A (n x m)
A = matrix(R, n, m, [R.random_element() for _ in range(n*m)])
print("A:\n", A)

# Noise e (vector of length m)
e_vec = sample_noise(m)
print("noise e (vector):", e_vec)

# To compute s.T * A, we treat s and e as matrices
# Converts the vector s to a 1-row matrix
# Converts the vector e to a 1-row matrix
s_mat = matrix(s_vec) 
e_mat = matrix(e_vec) 

# Public vector b (length m), computed via transpose
# b.T = s.T * A + e.T
bT = s_mat * A + e_mat       # No transpose needed on s_mat, as it's already a row
b = vector(R, bT[0])  # Convert back to a vector
print("b.T = s*A + e:", bT)
print("b:", b)

# 4) Encryption of a single bit
msg = R(randrange(2))
print("\nmessage:", msg)

# Random vector r (length m)
r = vector(R, [randrange(2) for _ in range(m)])
print("r:", r)

# Ciphertext component u
# u = A*r (vector of length n)
u = A * r
print("u = A*r:", u)

# Ciphertext component v
# v = b.T*r + msg*(q//2) which is the dot product
v = b.dot_product(r) + msg*(q//2)
print("v = b.T*r + msg*floor(q/2):", v)

# 5) Decryption
# Compute v' = v - s'*u which is v - s.dot_product(u)
dv = v - s_vec.dot_product(u) # Use the original s_vec for the dot product
print("\ndecryption value dv =", dv)

# Turn dv (element of R) into a standard integer
dv_int = Integer(dv)

# Decide based on distance to 0 vs. q/2
if dv_int <= q//4 or dv_int >= q - q//4:
    dec = 0
else:
    dec = 1

print("decrypted:", dec)
print("correct?", dec == Integer(msg))
