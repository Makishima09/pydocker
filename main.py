import pandas as pd
import matplotlib.pyplot as plt

# Carga el dataset de Tesla
file_path = 'Tesla_Dataset.csv'
tesla_data = pd.read_csv(file_path)

# Muestra las primeras filas del conjunto de datos para entender su estructura
print(tesla_data.head())

# Convertir la columna 'Date' a datetime
tesla_data['Date'] = pd.to_datetime(tesla_data['Date'])

# Ordenar los datos por fecha
tesla_data = tesla_data.sort_values('Date')

# Grafico 1: Evolución del precio de cierre ajustado a lo largo del tiempo
plt.figure(figsize=(10, 6))
plt.plot(tesla_data['Date'], tesla_data['Adj Close'], label='Adjusted Close Price')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.title('Evolution of Adjusted Close Price over Time')
plt.legend()
plt.grid(True)
#plt.show()
plt.savefig('adjusted_close_price.png')  # Guardar como imagen
plt.close()

# Grafico 2: Volumen de transacciones a lo largo del tiempo
plt.figure(figsize=(10, 6))
plt.plot(tesla_data['Date'], tesla_data['Volume'], label='Volume', color='orange')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.title('Volume of Transactions over Time')
plt.legend()
plt.grid(True)
#plt.show()
plt.savefig('volume_of_transactions.png')  # Guardar como imagen
plt.close()


# Grafico 3: Comparación de los precios de apertura y cierre a lo largo del tiemp
plt.figure(figsize=(10, 6))
plt.plot(tesla_data['Date'], tesla_data['Open'], label='Opening Price', color='green')
plt.plot(tesla_data['Date'], tesla_data['Close'], label='Closing Price', color='red')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Comparison of Opening and Closing Prices over Time')
plt.legend()
plt.grid(True)
#plt.show()
plt.savefig('opening_vs_closing_prices.png')  # Guardar como imagen
plt.close()
