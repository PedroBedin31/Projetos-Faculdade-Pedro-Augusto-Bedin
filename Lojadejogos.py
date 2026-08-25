nome = str(input("Digite seu nome completo: "))
nome_jogo = str(input("Digite o nome do jogo: "))
preco_jogo = float(input("Digite o preço do jogo: "))
print("\nFORMAS DE PAGAMENTO (DESCONTO): \n Dinheiro/Pix(10%) digite: 1 \n Cartão á vista(5%) digite: 2")
print(" Cartão parcelado(0%) digite: 3 \n Boleto(15%) digite: 4\n")
forma_de_pagamento = int(input("Digite o tipo de pagamento: "))

if forma_de_pagamento == 1:
    preco_jogo = preco_jogo * 0.90
elif forma_de_pagamento == 2:
    preco_jogo = preco_jogo * 0.95
elif forma_de_pagamento == 3:
    preco_jogo = preco_jogo
elif forma_de_pagamento == 4:
    preco_jogo = preco_jogo * 0.85

print("---------- LOJA DE JOGOS ----------")
print(f"Nome: {nome}")
print(f"Jogo: {nome_jogo}")
print(f"Preço final: {preco_jogo: .2f}")
