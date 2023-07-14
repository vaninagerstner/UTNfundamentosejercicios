import matplotlib.pyplot as plt

# Datos de ejemplo para las lluvias mensuales
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
lluvias = [50, 60, 40, 30, 70, 80, 90, 100, 80, 70, 60, 50]

# Crear gráfico de barras
plt.bar(meses, lluvias, color='red')

# Configurar etiquetas de los ejes
plt.xlabel('Meses')
plt.ylabel('Lluvias (mm)')
plt.title('Evolución de las lluvias mensuales')

# Mostrar el gráfico
plt.show()



