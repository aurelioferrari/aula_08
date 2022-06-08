import math

c1 = float(input("Valor do primeiro cateto: "))
c2 = float(input("Valor do segundo cateto: "))

c1_2 = c1**2
c2_2 = c2**2

soma = c1_2 + c2_2

hipotenusa = math.sqrt(soma)

print("A hipotenusa mede: {:}".format(hipotenusa))