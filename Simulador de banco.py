print("Bienvenido al programa de Saldo: PagoMovil")

saldo = 500
off = 1
op = 0

while off == 1:
	
	tr = ""
	dep = 0
	
	print("""Seleccione las opciones por numero
	
	1 • Consultar su Saldo
	2 • Depositar Dinero
	3 • Retirar Dinero
	4 • Realizar una transferencia
	5 • Salir del programa
	
     """)
	
	op = int(input("Introduce tu opcion "))
	
	if op == 1:
		print("\nTu saldo es de", saldo, "Bs\n")
		
	elif op == 2:
		print("\nCuanto dinero quieres depositar?")
		dep = int(input(">>> "))
		saldo = saldo + dep
		print("\nTu saldo ha sido actualizado! Tu saldo es de:", saldo, "Bs")
	
	elif op == 3:
		print("\nCuanto dinero quieres retirar?")
		dep = int(input(">>> "))
		if saldo < dep:
			print("No tienes el Saldo suficiente!")
		else:
			saldo = saldo - dep
			print("\nTu saldo ha sido actualizado! Tu saldo es de:", saldo, "Bs")
	
	elif op == 4:
		print("\nCuanto dinero quieres trasferir?")
		dep = int(input(">>> "))
		if saldo < dep:
			print("No tienes el Saldo suficiente!")
		else:
			print("\na quien deseas enviar?")
			tr = str(input(">>> "))
			saldo = saldo - dep
			print("\nTu saldo ha sido actualizado! Tu saldo es de:", saldo, "Bs, y se envio a", tr'')
	
	
	elif op == 5:
		break
		
	else:
		print("por favor selecciona una opcion valida")
		
print("\nGracias por usar, reinicia para usar de nuevo")
		