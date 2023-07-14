nacimiento = int(input("Ingrese su año de nacimiento: "))
actual = 2023
edad = actual - nacimiento

if edad >= 18:
    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")
