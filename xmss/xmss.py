from wots import *

#this is not a real tree. Just an example created manually
#i am not using L trees also :)

sks = []


class Tree:
    def __init__(self, data, left, right, parent):
       self.left = left
       self.right = right
       self.parent = parent
       self.data = data

    def setData(self, data):
       self.data = data

def key_concatenate(key1, key2):
    concat = key1 + key2
    concat = b''.join(concat) #makes the list into a single byte string
    return hashlib.sha256(concat).digest()

# ------ FIRST TREE -------------#
#gera wots key de 32 elementos
sk0 = gen_sk(32)
#gera wots public key
pk = gen_pk(sk0, 256)
#gera 1 folha
leaf1 = Tree(pk, None, None, None)


#gera wots key de 32 elementos
sk = gen_sk(32)
#gera wots public key
pk = gen_pk(sk, 256)
#gera outra folha
leaf2 = Tree(pk, None, None, None)

root = Tree( key_concatenate(leaf1.data, leaf2.data), leaf1, leaf2, None )
leaf1.parent = root
leaf2.parent = root

#---------- public key ----------------#
root.data
#------#-----------#--------#--------#

#second level tree
sk = gen_sk(32)
sks.append(sk)
#gera wots public key
pk = gen_pk(sk, 256)
#gera 1 folha
leaf11 = Tree(pk, None, None, None)

#gera wots key de 32 elementos
sk = gen_sk(32)
sks.append(sk)
#gera wots public key
pk = gen_pk(sk, 256)
#gera outra folha
leaf22 = Tree(pk, None, None, None)

root2 = Tree( key_concatenate(leaf11.data, leaf22.data), leaf11, leaf22, None )
leaf11.parent = root2
leaf22.parent = root2

#---------------#------------------------

auth = signMessage(sk0, root2.data)

#---------------#------------------------


#usando mensagem de 16 bits
message = "abacatecomacucaramareloemuitbom"
b_message = message.encode('utf-8')   #converte para bytes


#obtem assinatura
sign = signMessage(sks[0], b_message)


#assinatura = [message, sign, leaf11, leaf22, auth, leaf1, leaf2]
verify(b_message, sign, leaf11.data)

cert = key_concatenate(leaf11.data, leaf22.data)

verify(cert, auth, leaf1.data)


cert = key_concatenate(leaf1.data, leaf2.data)


assert cert == root.data









