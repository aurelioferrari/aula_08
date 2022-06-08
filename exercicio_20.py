import random

nome1 = str(input("Primeiro aluno: "))
nome2 = str(input("Segundo aluno: "))
nome3 = str(input("Terceiro aluno: "))
nome4 = str(input("Quarto aluno: "))

lista = [nome1, nome2, nome3, nome4]

random.shuffle(lista)

print("O primeiro alune é: {}" .format(lista[0]))
print("O segundo alune é: {}" .format(lista[1]))
print("O terceiro alune é: {}" .format(lista[2]))
print("O quarto alune é: {}" .format(lista[3]))