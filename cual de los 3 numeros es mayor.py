print("============================================")
print("*Sistema de saber cual numero es mas grande*")
print("============================================\n")

print("ingrese el primer numero a calcular...")
n1 = float(input(">"))
print("\ningrese el segundo numero a calcular...")
n2 = float(input(">"))
print("\ningrese el tercer numero a calcular...")
n3 = float(input(">"))

if n1 > n2 and n3:
    print("\nel numero ", n1, " es mayor de los tres")
elif n2 >  n1 and n3:
    print("\nel numero ", n2, " es mayor de los tres")
elif n3 > n1 and n2:
    print("\nel numero ", n3, " es mayor de los tres")
else:
    print("\nERROR, el sistema necesita numeros validos para calcular")
print("\n•reinicie el programa para poder usarlo de nuevo")