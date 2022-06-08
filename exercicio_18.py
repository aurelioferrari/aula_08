import math

numero = float(input("Digite um ângulo: "))

radiano = math.radians(numero)

cos = math.cos(radiano)
sen = math.sin(radiano)
tan = math.tan(radiano)

print("cosseno: {:.2f}".format(cos))
print("seno: {:.2f}".format(sen))
print("tangente: {:.2f}".format(tan))