import matplotlib.pyplot as plt
# Datos de ejemplo de temperatura en Choele Choel (°C) tomada cada hora a lo largo de un día
temperaturas_choele_choel = [28, 28, 28, 29, 30, 31, 32, 33, 33, 32, 31, 30, 29, 28, 28, 29, 30, 31, 32, 32, 32, 31, 30, 29]
# Datos de ejemplo de temperatura en Tafí del Valle (°C) tomada cada hora a lo largo de un día
temperaturas_tafi_del_valle = [18, 18, 18, 18, 17, 16, 16, 15, 15, 16, 17, 18, 19, 20, 20, 20, 19, 18, 17, 17, 17, 18, 18, 18]
# Horas del día correspondientes a las temperaturas
horas = range(0, 24)
# Crear el gráfico
plt.plot(horas, temperaturas_choele_choel, marker='o', label='Choele Choel')
plt.plot(horas, temperaturas_tafi_del_valle, marker='o', label='Tafí del Valle')
# Configurar los ejes del gráfico
plt.xlabel('Hora')
plt.ylabel('Temperatura (°C)')
# Agregar título al gráfico
plt.title('Evolución de la temperatura en Choele Choel y Tafí del Valle')
# Agregar una leyenda
plt.legend()
# Mostrar el gráfico
plt.show()
