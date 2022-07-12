# nombre= input("Indroduzca su nombre: ")

# print("Hola" + nombre )

# resultado = (((2+3)/10)**2)

# print(resultado)

def calculadora(horas_de_trabajo, pago_por_hora):
    horas_de_trabajo = input("Introduzca horas trabajadas: ")
    pago_por_hora = input("Introduzca el pago por hora de trabajo: ")
    salario = (horas_de_trabajo * pago_por_hora)
    print("Su pago es de: " + salario)
    
if __name__ == '__main__':
    calculadora()
 
