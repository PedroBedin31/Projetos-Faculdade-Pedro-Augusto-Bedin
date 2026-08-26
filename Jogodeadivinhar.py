import random
import os

print("----------------------ADIVINHE O NÚMERO----------------------")
print("            REGRAS: Escolha um número de 1 a 100             ")
print("O computador irá gerar um número aleatório, tente adivinha-lo")
print("-------------------------------------------------------------")

input("Clique o botão ENTER para continuar... ")

numero_secreto = random.randint(1, 100)

palpite = int(input("Digite um número de 1 a 100 "))
tentativas = 1

while palpite != numero_secreto:
    if palpite < numero_secreto:
        print(f"ERRADO!! Tente um número MAIOR!!!")
        palpite = int(input("Digite novamente "))
        tentativas += 1
    elif palpite > numero_secreto:
        print(f"ERRADO!! Tente um número MENOR!!!")
        palpite = int(input("Digite novamente "))
        tentativas += 1

if palpite == numero_secreto:
    print("---------- PARABÉNS, VOCÊ GANHOU!!! ----------")
    print(f"Número secreto: {numero_secreto} ")
    print(f"Tentativas: {tentativas}")

