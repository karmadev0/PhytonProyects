print("====================================")
print("Sistema de igualdades de par e impar")
print("====================================\n")
print("porfavor, escriba un numero para verificar si es par o impar")
numero = int(input(">"))
resultado = (numero) % 2
if resultado == 1:
    print("\nel numero ", numero, " es impar.")
elif resultado == 0:
    print("\nel numero ", numero, " es par.")
else:
    print("\nERROR, reinicie el programa e intentelo denuevo y coloque un numero entero valido")
print("\nreinicie el programa para volver a usar")
