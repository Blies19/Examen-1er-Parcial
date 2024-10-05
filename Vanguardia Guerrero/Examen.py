import pandas as pd

# Cargar los datos
df_flights = pd.read_csv('flights.csv')

# Ver las primeras filas
df_flights.head()

# Verificar valores nulos
df_flights.isnull().sum()

# Imputar valores nulos en DepDelay y ArrDelay con la media
df_flights['DepDelay'].fillna(df_flights['DepDelay'].mean(), inplace=True)
df_flights['ArrDelay'].fillna(df_flights['ArrDelay'].mean(), inplace=True)

# Definir un umbral de 3 desviaciones estándar para eliminar outliers
dep_delay_threshold = df_flights['DepDelay'].mean() + 3 * df_flights['DepDelay'].std()
arr_delay_threshold = df_flights['ArrDelay'].mean() + 3 * df_flights['ArrDelay'].std()

# Filtrar los valores fuera de ese umbral
df_flights = df_flights[(df_flights['DepDelay'] < dep_delay_threshold) & (df_flights['ArrDelay'] < arr_delay_threshold)]

# Resumen estadístico de las columnas numéricas
df_flights.describe()

import matplotlib.pyplot as plt

# Histograma de retrasos de salida
plt.hist(df_flights['DepDelay'], bins=50, color='blue', alpha=0.7)
plt.title('Distribución de los retrasos de salida')
plt.xlabel('Retraso en minutos')
plt.ylabel('Frecuencia')
plt.show()

# Histograma de retrasos de llegada
plt.hist(df_flights['ArrDelay'], bins=50, color='green', alpha=0.7)
plt.title('Distribución de los retrasos de llegada')
plt.xlabel('Retraso en minutos')
plt.ylabel('Frecuencia')
plt.show()

# Retraso promedio de salida y llegada
mean_dep_delay = df_flights['DepDelay'].mean()
mean_arr_delay = df_flights['ArrDelay'].mean()

print(f'Retraso promedio de salida: {mean_dep_delay:.2f} minutos')
print(f'Retraso promedio de llegada: {mean_arr_delay:.2f} minutos')

# Retraso promedio de llegada por aerolínea
arrival_delay_by_carrier = df_flights.groupby('Carrier')['ArrDelay'].mean().sort_values()

print(arrival_delay_by_carrier)

# Retraso promedio de llegada por día de la semana
arrival_delay_by_day = df_flights.groupby('DayOfWeek')['ArrDelay'].mean().sort_values()

print(arrival_delay_by_day)

# Aeropuerto con mayor retraso promedio de salida
dep_delay_by_airport = df_flights.groupby('OriginAirportName')['DepDelay'].mean().sort_values(ascending=False)

print(dep_delay_by_airport.head(1))

# Comparar vuelos que salen a tiempo (DepDelay <= 0) vs vuelos que salen tarde (DepDelay > 0)
on_time_departures = df_flights[df_flights['DepDelay'] <= 0]['ArrDelay'].mean()
late_departures = df_flights[df_flights['DepDelay'] > 0]['ArrDelay'].mean()

print(f'Retraso promedio de llegada (vuelos a tiempo): {on_time_departures:.2f} minutos')
print(f'Retraso promedio de llegada (vuelos tardíos): {late_departures:.2f} minutos')

# Crear una columna para identificar la ruta (Origen -> Destino)
df_flights['Route'] = df_flights['OriginAirportName'] + ' -> ' + df_flights['DestAirportName']

# Ruta con más llegadas tarde (ArrDelay15 == 1)
late_arrivals_by_route = df_flights[df_flights['ArrDelay15'] == 1].groupby('Route').size().sort_values(ascending=False)

print(late_arrivals_by_route.head(1))

# Ruta con mayor retraso promedio de llegada
mean_arr_delay_by_route = df_flights.groupby('Route')['ArrDelay'].mean().sort_values(ascending=False)

print(mean_arr_delay_by_route.head(1))
