def conversor(tipo_de_moneda, valor_dolar, valor_pesos):
    tipo_de_moneda = input("ingrese cantidad de " + tipo_de_moneda + ": ")
    tipo_de_moneda = float(tipo_de_moneda)
    valor_Btc = 41357.41
    valor_Eth = 3981.4
    dolares = tipo_de_moneda / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    Btc = (tipo_de_moneda / valor_dolar) / valor_Btc
    Btc = round(Btc, 2)
    Btc = str(Btc)
    Eth = (tipo_de_moneda / valor_dolar) / valor_Eth
    Eth = round(Eth, 2)
    Eth = str(Eth)
    pesos = tipo_de_moneda * valor_pesos
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print("Tienes $ " + dolares + " dolares")
    print("Tienes " + Btc + " Bitcoins")
    print("Tienes " + Eth + " Ether")
    print("Tienes " + pesos + " pesos colombianos")


menu = """
Bienvenidos al cenversor de monedas multiples 💵💴💶💲

1- Bolivares
2- Euros
3- Pesos Mexicanos

Elige una opción:

"""
opcion = int(input(menu))

if opcion == 1:
    conversor("Bolivares", 4.73, 3700)
elif opcion == 2:
    conversor("Euros", 0.80, 4000)
elif opcion == 3:
    conversor("Pesos mexicanos", 20, 201)
else:
    print("Introduzca una opcion correcta, por favor.")
