import random
import os

print("----------------------ADIVINHE O NÚMERO----------------------\n")
print("O computador irá gerar um número aleatório, tente adivinha-lo\n")
print("-------------------------------------------------------------")

print("            Dificuldade: Fácil (1 a 100)                      ")
print("            Difculdade: Médio (1 a 500)                      ")
print("            Difculdade: Difícil (1 a 1000)                   ")

dificuldade = int(input("Escolha a dificuldade: facil(1), medio(2) ou dificil(3): "))

if dificuldade == 1:
    numero_secreto = random.randint(1, 50)
elif dificuldade == 2:
    numero_secreto = random.randint(1, 500)
else:
    numero_secreto = random.randint(1, 1000)

palpite = int(input("Digite um número: "))
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
