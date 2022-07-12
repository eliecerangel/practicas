def run():
    LIMITE = 1001

    cuenta = 0
    ingresos_mensuales = int(input('Escribe un numero: '))
    saldo_total = (cuenta + ingresos_mensuales)
    while saldo_total < LIMITE:
        print('Saldo actual es: ' + str(saldo_total))
        cuenta = saldo_total
        saldo_total = cuenta + ingresos_mensuales
            

if __name__ == '__main__':
    run()