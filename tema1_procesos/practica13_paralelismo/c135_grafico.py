import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo de resultados
data = pd.read_csv('resultados.csv', names=['num_procesos', 'tiempo_total', 'total_primos'])

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(data['num_procesos'], data['tiempo_total'], marker='o', linestyle='-', color='b')
plt.title("Evolución del Tiempo vs Número de Procesos")
plt.xlabel("Número de Procesos")
plt.ylabel("Tiempo Total (segundos)")
plt.grid(True)
plt.show()

