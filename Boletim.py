nome = str(input("Digite o seu nome: "))
disciplina = str(input("Digite o seu disciplina: "))
nota = int(input("Digite o valor da nota: "))

print("----------BOLETIM DE NOTAS----------")
print(f"Seu nome: {nome}")
print(f"Disciplina: {disciplina}")
print(f"Sua nota: {nota}")

if nota >= 0 and nota <= 39:
    print("RESULTADO: VOCÊ FOI REPROVADO! ")
elif nota >= 40 and nota <= 59:
    print("RESULTADO: VOCÊ ESTÁ DE RECUPERAÇÃO! ")
elif nota >= 60 and nota <= 100:
    print(f"RESULTADO: VOCÊ FOI APROVADO! ")

print("----------BOLETIM DE NOTAS----------")
