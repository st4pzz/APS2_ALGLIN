from funcoes import para_one_hot,para_string,cifrar, de_cifrar, enigma, de_enigma
import numpy as np
from colorama import init, Fore, Style

#implemntando alfebeto e encoder
alfabeto = 'abcdefghijklmnopqrstuvwxyz ãé,.'
alfabeto_identidade = np.identity(len(alfabeto))
encoder = np.roll(alfabeto_identidade,-2,1)
segundo_encoder = np.roll(alfabeto_identidade,7,1)

print()
print(Fore.RED + "FUNCOES: para_one_hot, para_string, cifrar, de_cifrar")
print("-----------------------------------------------------"+ Style.RESET_ALL)
print()
print("-> testando one_hot, para_string, cifrar e de_cifrar com a mensagem 'eu sou o goku'")
print()

#one_hot
# msg = 'eu sou o goku'
# one_hot = para_one_hot(msg)
# print(Fore.BLUE + "one_hot:" + Style.RESET_ALL)
# print()
# print(one_hot)
# print()

# msg = "gay"
# one_hot = para_one_hot(msg)
# msg = para_string(one_hot)
# print(Fore.BLUE + "para_string:" + Style.RESET_ALL)
# print()
# print(msg)
# print()

# cifrar
# msg = "eu sou o goku"
# one_hot = para_one_hot(msg)
# msg_cifrada = cifrar(msg,encoder)
# print(Fore.BLUE + "cifrar:" + Style.RESET_ALL)
# print()
# print(msg_cifrada)
# print()

#de_cifrar
# msg = "eu sou o goku"
# one_hot = para_one_hot(msg)
# msg_cifrada = cifrar(msg,encoder)
# msg_decifrada = de_cifrar(msg_cifrada,encoder)
# print(Fore.BLUE + "de_cifrar:" + Style.RESET_ALL)
# print()
# print(msg_decifrada)
# print()

# print()
# print(Fore.RED + "FUNCOES: enigma, de_enigma" + Style.RESET_ALL)
# print(Fore.RED +"-----------------------------------------------------" + Style.RESET_ALL)
# print()
# print("-> testando enigma e de_enigma com a mensagem 'eu estou com fome'")
# print()
#enigma
msg = "eu estou com fome"
one_hot = para_one_hot(msg)
msg_cifrada = cifrar(msg,encoder)
msg_enigma = enigma(msg,encoder,segundo_encoder)
print(Fore.BLUE + "enigma:" + Style.RESET_ALL)
print()
print(msg_enigma)
print()
#de_enigma
# msg = "eu estou com fome"
# one_hot = para_one_hot(msg)
# msg_cifrada = cifrar(msg,encoder)
# msg_enigma = enigma(msg,encoder,segundo_encoder)
# msg_de_enigma = de_enigma(msg_enigma,encoder,segundo_encoder)
# print(Fore.BLUE + "de_enigma:" + Style.RESET_ALL)
# print()
# print(msg_de_enigma)
# print()


