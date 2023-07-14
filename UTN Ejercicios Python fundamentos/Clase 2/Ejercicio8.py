peso = float(input("Ingrese el peso en Kg:  "))
altura = float(input("Ingrese la altura en Mts: "))
imc= round(peso / (altura ** 2), 2)
print("El IMC de la persona es de", imc )
