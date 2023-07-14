import matplotlib.pyplot as plt
# Datos de ejemplo de la temperatura tomada cada hora a lo largo de un día
temperaturas = [23, 23, 23, 24, 25, 26, 27, 28, 29, 30, 30, 31, 32, 32, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23]
# Horas del día correspondientes a las temperaturas
horas = range(0, 24)
# Crear el gráfico
plt.plot(horas, temperaturas, color='blue')
# Rellenar el área bajo la curva
plt.fill_between(horas, temperaturas, color='lightblue')
# Configurar los ejes del gráfico
plt.xlabel('Hora')
plt.ylabel('Temperatura (°C)')
# Agregar título al gráfico
plt.title('Evolución de la temperatura durante un día')
# Mostrar el gráfico
plt.show()
