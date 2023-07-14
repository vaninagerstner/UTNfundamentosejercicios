edad = int(input("Ingrese su edad: "))
if edad < 2:
    valor = 0
elif edad <= 4:
    valor = 100
elif edad <= 10:
    valor = 200
elif edad <= 18:
    valor = 400
elif edad >= 65:
    valor = 500
else:
    valor = 1000
print("Debe abonar " + str(valor) + " pesos para ingresar al parque.")

