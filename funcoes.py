import numpy as np


def para_one_hot(msg: str):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    msg = msg.lower()
    one_hot = np.zeros((len(msg),len(alfabeto)))
    for i in range(len(msg)):
        one_hot[i][alfabeto.find(msg[i])] = 1
    return one_hot.T
    
def para_string(M : np.array):
    return
def cifrar(msg: str,P : np.array):
    return
def de_cifrar(msg: str,P : np.array):
    return
def enigma(msg: str, P : np.array, E : np.array):
    return
def de_enigma(msg: str, P : np.array, E : np.array):
    return