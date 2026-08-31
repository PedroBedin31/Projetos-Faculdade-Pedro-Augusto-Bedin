import os
import sys 

def reiniciar_programa():
    precotijolos = 1.50 
    precocimento = 60
    precotinta   = 500 

    orcamento = float(input("Digite o limite do orçamento em R$: "))
    tijolos   = int(input("Digite a quantidade de tijolos - R$1,50 : "))

    totaltijolos = precotijolos * tijolos 

    while totaltijolos > orcamento:
        print("Orçamento estourado!!")
        tijolos = int(input("Digite a quantidade de tijolos - R$1,50 : "))
        totaltijolos = precotijolos * tijolos

    cimento = int(input("Digite a quantidade de cimento(sacos) - R$60 : "))
    totalcimento = precocimento * cimento 

    while totalcimento + totaltijolos > orcamento:
        print("Orçamento estourado!!")
        print("Deseja começar novamente? (S/N)")
        resposta = input().upper()
        if resposta == "S":
            reiniciar_programa()
            return
        else:
            cimento = int(input("Digite a quantidade de cimento(sacos) - R$60 : "))
            totalcimento = precocimento * cimento

    tinta = int(input("Digite a quantidade de tinta(latas) - R$100 : "))
    totaltinta = precotinta * tinta
  
    while totaltinta + totalcimento + totaltijolos > orcamento:
        print("Orçamento estourado!!")
        print("Deseja começar novamente? (S/N)")
        resposta = input().upper()
        if resposta == "S":
            reiniciar_programa()
            return
        else:
            tinta = int(input("Digite a quantidade de tinta(latas) - R$100 : "))
            totaltinta = precotinta * tinta

    print(f"Total tijolos: R$ {totaltijolos}")
    print(f"Total cimento: R$ {totalcimento}")
    print(f"Total tinta: R$ {totaltinta}")

    soma_tudo = totaltijolos + totalcimento + totaltinta 

    if soma_tudo > orcamento:
        print("Orçamento estourado!!")
    else:
        print("Dentro do orçamento!")
        print(f"Total: R${soma_tudo} ")


reiniciar_programa()
