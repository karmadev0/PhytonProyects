print("====================")
print("Sistema de determinacion de vacaciones para trabajadores")
print("====================\n")

print("Porfavor ingrese el nombre del trabajador")
nombre = input(">")

print("\nPorfavor ingrese la clave de departamento a que corresponde el trabajador:")
print("1: atención al cliente, 2: logistica, 3: gerencia")
opcion = int(input(">"))
if opcion == 1:
    print("\ningrese la antiguedad de años que tiene en numero")
    atc = int(input(">"))
    if atc <= 0:
        print("\n'" + nombre + "' no merece dias de vacaciones")
    elif atc == 1:
        print("\nlos dias de vacaciones que merece '" + nombre + "' serian: 6 dias.")
    elif atc >= 2 and atc <= 6:
        print("\nlos dias de vacaciones que merece '" + nombre + "' serian: 14 dias.")
    else:
        print("\nlos dias de vacaciones que merece '" + nombre + "' serian: 20 dias.")
            
elif opcion == 2:
    print("\ningrese la antiguedad de años que tiene en numero")
    log = int(input(">"))
    if log <= 0:
        print("\n'" + nombre + "' no merece dias de vacaciones")
    elif log == 1:
        print("\nlos dias de vacaciones que merece '" + nombre + "' serian: 7 dias.")
    elif log >= 2 and log <= 6:
        print("\nlos dias de vacaciones que merece '" + nombre + "' serian: 15 dias.")
    else:
        print("\nlos dias de vacaciones que merece '" + nombre + "' serian: 22 dias.")
            
elif opcion == 3:
    print("\ningrese la antiguedad de años que tiene en numero")
    ger = int(input(">"))
    if ger <= 0:
        print("\n'" + nombre + "' no merece dias de vacaciones")
    elif ger == 1:
        print("\nlos dias de vacaciones que merece '" + nombre + "' serian: 10 dias.")
    elif ger >= 2 and ger <= 6:
        print("\nlos dias de vacaciones que merece '" + nombre + "' serian: 20 dias.")
    else:
        print("\nlos dias de vacaciones que merece '" + nombre + "' serian: 30 dias.")
            
else:
    print("\nlo sentimos, esa opcion no esta disponible")
    print("porfavor reincie el programa y intentelo denuevo")