print("""--------------------------
=== Calculadora pyhton ===

v1.0.0, creado por karmagmr0, made in python
--------------------------\n""")
print("* Menu de opciones *\n")
print("""1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division entera
6. Exponentes
7. Modulo o resto \n""")
numero = int(input(">"))

if numero == 1:
    print("Has seleccionado 'Suma'")
    print("porfavor ingrese el primer digito a sumar...\n")
    numero = float(input(">"))
    print("porfavor ingrese el segundo digito a sumar... \n")
    numero += float(input(">"))
    print("la suma seria: ", numero)
    
elif numero == 2:
    print("has seleccionado 'Resta'")
    print("porfavor ingrese el primer digito a restar... \n")
    numero = float(input(">"))
    print("porfavor ingrese el segundo digito a restar... \n")
    numero -= float(input(">"))
    print("la resta seria: ", numero)
    
    
elif numero == 3:
    print("has seleccionado 'Multiplicacion'")
    print("porfavor ingrese el primer digito a multiplicar... \n")
    numero = float(input(">"))
    print("porfavor ingrese el segundo digito a multiplicar... \n")
    numero *= float(input(">"))
    print("la multiplicacion seria: ", numero)
    
elif numero == 4:
    print("has seleccionado 'Division'")
    print("porfavor ingrese el primer digito a dividir... \n")
    numero = float(input(">"))
    print("porfavor ingrese el segundo digito a dividir... \n")
    numero /= float(input(">"))
    print("la division seria: ", numero)

elif numero == 5:
    print("has seleccionado 'Division entera'")
    print("porfavor ingrese el primer digito a dividir enteramente... \n")
    numero = float(input(">"))
    print("porfavor ingrese el segundo digito a dividir enteramente... \n")
    numero //= float(input(">"))
    print("la division entera seria: ", numero)
    
elif numero == 6:
    print("has seleccionado 'Exponentes'")
    print("porfavor ingrese el primer digito a exponer... \n")
    numero = int(input(">"))
    print("porfavor ingrese el segundo digito a exponer... \n")
    numero **= int(input(">"))
    print("el exponente completo seria: ", numero)

elif numero == 7:
    print("has seleccionado 'Modulo o resto'")
    print("porfavor ingrese el primer digito a dividir (modulo)... \n")
    numero = float(input(">"))
    print("porfavor ingrese el segundo digito a dividir (modulo)... \n")
    numero %= float(input(">"))
    print("el modulo o resto de ello seria: ", numero)
    
else:
    print("opcion invalida, porfavor reinicie el programa y seleccione una opcion valida")
print("reincie el programa para poder volver a usarlo")