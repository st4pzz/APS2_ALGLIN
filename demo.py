from funcoes import para_one_hot,para_string,cifrar, de_cifrar
import numpy as np


msg = 'abc'
one_hot = para_one_hot(msg)
# print(one_hot)


msg2 = para_string(one_hot)
# print(msg2)

P = np.array( [[1,0,0],[0,1,0],[0,0,1]])
ms3 = cifrar(msg,P)
#print(ms3)

P = np.array( [[0,0,1],[1,0,0],[0,1,0]])
msg4 = de_cifrar(msg,P)
print(msg4)

