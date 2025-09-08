#https://doc.sagemath.org/html/en/thematic_tutorials/numtheory_rsa.html


p = 2^31 - 1
q = 2^61 - 1

n = p * q

phi = (p - 1)*(q - 1)

e = ZZ.random_element(phi)   #retorna inteiro aleatório de [0, phi]
while (gcd(e, phi) != 1):
    e = ZZ.random_element(phi)   #retorna inteiro aleatório de [0, phi]
    
    
#e.d = 1 mod φ(n)  == ed mod φ(n) = 1 
#se ed / φ(n) = x então ed % φ(n) = 1
#podemos reescrever como
#ed - x.φ(n) = 1

#Bézout identity gcd(x, y) = sx + ty 


bezout = xgcd(e, phi)   # (g, s, t) tal que gcd(e, phi) = e.x + phi.y 
			# lembre que gcd(e, phi) == 1
			# portanto, podemos escrever que 1 = e*x + phi.y
		        # d = x
			

#extended Euclidean algorithm 
 		
			
d = Integer(mod(bezout[1], phi)) 

print(d)

private_key = [d, e, n]
public_key = [e, n]

m = "mensagem"

mb = [ord(k) for k in m]

print(mb)

#transforma em elemento de Z
x = ZZ(list(reversed(mb)), 256)


cifred = power_mod(x, e, n)


print(cifred)

decifred = power_mod(cifred, d, n)


print(decifred)

L = decifred.digits(256)

mb_recuperado = list(reversed(L))

print(mb_recuperado)



   


