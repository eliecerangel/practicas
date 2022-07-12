# edad = int(input("Escribe tu edad: "))
# if edad >= 18:
#     print("Eres apto para entrar")
# else:
#     print("No eres apto para entrar")

# numero = int(input("Escribe un numero: "))
# if numero > 100:
#     print("Es mayor a 100")
# elif numero == 100:
#     print("Es igual a 100")
# else:
#     print("Es menor a 100")

caucho = input("Escriba su tipo de caucho (tipo A o B): ")
if caucho == "A":
    print("El costo es de 100 dolares")
    costoA = 100
    dolaresA = str(int(input("Escriba la cantidad que necesita: ")) * costoA)
    print("El costo total es de " + dolaresA + "dolares")
elif caucho == "B":
    print("El costo es de 80 dolares")
    costoB = 80
    dolaresB = str(int(input("Escriba la cantidad que necesita: ")) * costoB)
    print("El costo total es de " + dolaresB + " dolares")
else:
    print("ERROR TIPO NO COMPATIBLE")