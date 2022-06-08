import random

nome1 = str(input("Primeiro aluno: "))
nome2 = str(input("Segundo aluno: "))
nome3 = str(input("Terceiro aluno: "))
nome4 = str(input("Quarto aluno: "))

lista = [nome1, nome2, nome3, nome4]

numero = random.randint(0, 3)

print("o aluno que apagará o quadro será: {}".format(lista[numero]))