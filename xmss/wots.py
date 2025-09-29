

import hashlib 
import random


#gera a chave secreta (SK) com as listas 0 e 1. 
def gen_sk(size):
    l0 = [] 
    for x in list(range(0,size)):
        l0.append(random.randrange(0, 2**32).to_bytes(8, 'big'))    #converte numero para bytes no bigendian
    return l0
    
    
#faz o hash n vezes
def hash_n(sk, n):
    out = sk
    for _ in range(n):
        out = hashlib.sha256(out).digest()
    return out

#faz o hash n vezes pra todas as chaves privadas
def gen_pk(l, n):
    return [hash_n(x, n) for x in l]

#gera uma assinatura baseado nos bytes da mensagem
def signMessage(sk, message):
    return [hash_n(sk[i], b) for i, b in enumerate(message)]
    
#verifica usando a chave publica e assinatura
#caso a o byte da mensagem seja 0, fazemos o hash da assinatura e comparamos com pk[0...size]      
def verify(message, signature, pk):
    for index, byte in enumerate(message):
       value = 256 - int(byte)
       hashed = hash_n(signature[index], value)
       if(hashed != pk[index]): 
           print("falha na verificação")
           return
    print("mensagem verificada")

#usando mensagem de 16 bits
#message = "abacatecomacucaramareloemuitbom"

#b_message = message.encode('utf-8')   #converte para bytes

#bitString = byteToBit(b_message)

#gera secret key de 32 elementos
#sk = gen_sk(32)

#gera public key
#pk = gen_pk(sk, 256)

#obtem assinatura
#sign = signMessage(sk, b_message)

#b_message = "abacatecomacucaramareloemuitbom".encode('utf-8')

#verify(b_message, sign, pk)
