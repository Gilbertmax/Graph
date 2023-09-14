import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
producto_1_ventas = np.random.randint(100, 500, 12)  # Ventas mensuales del producto 1
producto_2_ventas = np.random.randint(200, 600, 12)  # Ventas mensuales del producto 2

# Crear el gráfico de barras con dos conjuntos de datos
plt.figure(figsize=(10, 6))  # Tamaño del gráfico
bar_width = 0.35  # Ancho de las barras

# Coordenadas para las barras
x = np.arange(len(meses))

plt.bar(x, producto_1_ventas, width=bar_width, label='Producto 1', color='blue', alpha=0.7)
plt.bar(x + bar_width, producto_2_ventas, width=bar_width, label='Producto 2', color='green', alpha=0.7)

# Etiquetas y título
plt.xlabel('Meses')
plt.ylabel('Ventas')
plt.title('Ventas Mensuales de Dos Productos en un Año')
plt.xticks(x + bar_width / 2, meses)  # Etiquetas en el eje x

# Leyenda
plt.legend()

# Mostrar el gráfico
plt.tight_layout()  # Ajustar márgenes
plt.show()
