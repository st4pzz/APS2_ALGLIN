import numpy as np


def para_one_hot(msg: str):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz '
    msg = msg.lower()
    one_hot = np.zeros((len(msg),len(alfabeto)))
    for i in range(len(msg)):
        one_hot[i][alfabeto.find(msg[i])] = 1
    return one_hot.T  
    
def para_string(M : np.array):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz '
    msg = ''
    for linha in M:
        for i in range(len(linha)):
            if linha[i] == 1:
                msg += alfabeto[i]
    return msg

    
def cifrar(msg: str,P : np.array):
    msg_one_hot = para_one_hot(msg)
    msg_cifrada = msg_one_hot@P
    return para_string(msg_cifrada)
    
def de_cifrar(msg: str,P : np.array):
    return
def enigma(msg: str, P : np.array, E : np.array):
    return
def de_enigma(msg: str, P : np.array, E : np.array):
    return