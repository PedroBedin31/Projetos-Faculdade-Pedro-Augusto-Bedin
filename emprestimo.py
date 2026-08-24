nome = str(input("Qual o seu nome? "))
idade = int(input("Qual a sua idade? "))
cpf = str(input("Qual o seu CPF? "))
salario = float(input("Digite seu salario: "))
emprestimo = float(input("Qual o valor do emprestimo? "))
validacao_garantia = str(input("Você possui algum bem para garantia?(S/N) "))

if validacao_garantia == "S" or validacao_garantia == "s":
    garantia = str(input("Qual o item da sua garantia? "))
    valor_do_bem = float(input("Qual o valor do bem? "))
else:
    valor_do_bem = 0
    garantia = " "

if emprestimo <= 100000:
    parcela = 2000
    if emprestimo > salario * 10 + valor_do_bem:
        resultado = "Seu emprestimo foi NEGADO!"
    else:
        resultado = "Seu emprestimo foi APROVADO!"
elif emprestimo >= 100000:
    parcela = 4000
    if emprestimo > salario * 10 + valor_do_bem:
        resultado = "Seu emprestimo foi NEGADO!"
    else:
        resultado ="Seu emprestimo foi APROVADO!"

print("-------EMPRESTIMO GERADO-------")
print(f"\nNome: {nome}")
print(f"Idade: {idade}")
print(f"CPF: {cpf}")
print(f"Salario: {salario}")
print(f"Emprestimo de: {emprestimo}")
print(f"Parcela: {parcela}")
print(f"Seu bem é: {garantia} e seu respectivo valor é: {valor_do_bem}!")
print(f"Resultado: {resultado}")
print("\n-------------------------------")


