print("""--------------------------
===Sistema de calcular el promedio de notas===

recuerde que esto es a base de la division entre 4 por las 4 notas, puede ser que otros utilicen otros metodos pero este es el mas popular

v1.0.0, creado por karmagmr0, made in python
--------------------------""")
nota1 = int(input("coloque la primera nota: "))
nota2 = int(input("coloque la segunda nota: "))
nota3 = int(input("coloque la tercera nota: "))
nota4 = int(input("coloque la cuarta nota: "))

promedio = (nota1 + nota2 + nota3 + nota4) / 4
promedio2 = (nota1 + nota2 + nota3 + nota4) // 4

print("-------------------------")

if promedio < 10:
    print("cagaste, raspaste por ", promedio, " puntos, vaya preparando las nalgas :'v"
", nota completa: ", promedio2)
if promedio == 10:
    print("a duras penas, cojeando y todo pero pasas por ", promedio, " puntos, si se pudo mano"
", nota completa: ", promedio2)
if promedio > 10:
    print("gg pa, pasaste por ", promedio, " puntos, hoy se celebra jijiji"
", nota completa: ", promedio2)