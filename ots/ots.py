

import hashlib 
import random


#convert string de bytes para lista de bits
def byteToBit(byteString):
    bitString = []
    for char in byteString:
        bits = format(char, "08b")                      #0:8b e formato binario
        bitString.extend(int(b) for b in bits)  
    return bitString

#gera a chave secreta (SK) com as listas 0 e 1. 
def gen_sk(size):
    l0 = [] 
    l1 = []
    for x in list(range(0,size)):
        l0.append(random.randrange(0, 32).to_bytes(8, 'big'))    #converte numero para bytes no bigendian
        l1.append(random.randrange(0, 32).to_bytes(8, 'big'))
    return [l0, l1]
    
#faz hash das duas listas l1 e l2 e retorna 
def gen_pk(l0, l1):
    return [hashlib.sha256(x).hexdigest() for x in l0 + l1]  
    

#gera uma assinatura baseado nos bits da mensagem
#se o bit é 1, inclui a chave privada da lista sk[1]
#senão sk[0]
def signMessage(sk, message):
    signature = []
    for b in list(range(0, len(message))):
       if message[b]: signature.append(sk[1][b])
       else: signature.append(sk[0][b])   
    return signature
    
#converte mensagem pra bits e verifica usando a chave publica e assinatura
#caso a o bit da mensagem seja 0, fazemos o hash da assinatura e comparamos com pk[0...size]
#senão comparamos o hash com pk[size+1, 2size]        
def verify(message, signature, pk):
    message = byteToBit(message)
    for index, bit in enumerate(message):
       idx = index + 256 if bit else index
       hashed = (hashlib.sha256(signature[index]).hexdigest())
       if(hashed != pk[idx]): 
           print("falha na verificação")
           return
    print("mensagem verificada")

#usando mensagem de 16 bits
message = "abacatecomacucaramareloemuitobom"

b_message = message.encode('utf-8')   #converte para bytes

bitString = byteToBit(b_message)

#gera secret key de 256 elementos
sk = gen_sk(256)

#gera public key
pk = gen_pk(sk[0], sk[1])

#obtem assinatura
sign = signMessage(sk, bitString)

#b_message = "abacatecomacucaramareloemuitobom".encode('utf-8')

verify(b_message, sign, pk)
