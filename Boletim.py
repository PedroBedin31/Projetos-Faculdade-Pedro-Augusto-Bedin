nome = str(input("Digite o seu nome: "))
curso = str(input("Digite o seu curso: "))
semestre = int(input("Digite o seu semestre: "))
disciplina = str(input("Digite o seu disciplina: "))
nota1 = int(input("Digite o valor da primeira nota: "))
nota2 = int(input("Digite o valor da segunda nota: "))
media = (nota1 + nota2) / 2

nota1 = max(0,min(nota1, 100))
nota2 = max(0,min(nota2, 100))
media = max(0, min(media, 100))
semestre = max(0, min(semestre, 12))

if media >= 0 and media <= 39:
    resultado = "VOCÊ FOI REPROVADO! "
elif media >= 40 and media <= 59:
    resultado = "VOCÊ ESTÁ DE RECUPERAÇÃO! "
elif media >= 60 and media <= 100:
    resultado = "VOCÊ FOI APROVADO! "

print("\n----------BOLETIM DE NOTAS----------")
print(f"Seu nome: {nome}")
print(f"Curso: {curso}")
print(f"Semestre: {semestre}")
print(f"Disciplina: {disciplina}")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Media: {media}")
print(f"Status: {resultado}") 
print("----------BOLETIM DE NOTAS----------")




