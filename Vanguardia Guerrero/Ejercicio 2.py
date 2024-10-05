# Importar las bibliotecas necesarias
from sklearn.datasets import fetch_openml
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Descargar la base de datos Titanic
titanic = fetch_openml('titanic', version=1, as_frame=True)

# Extraer el dataframe
df = titanic.frame

# Limpiar el dataframe, por ejemplo, eliminando los valores nulos en columnas críticas para gráficos
df_clean = df.dropna(subset=['age', 'fare', 'pclass', 'survived', 'sex'])

# Mostrar los primeros 5 registros para revisar los datos
print(df_clean.head())

# Obtener los parámetros estadísticos de todas las variables numéricas
print("\nParámetros estadísticos:")
print(df_clean.describe())

# Gráfico de barras para la variable 'sex' (categórica)
sns.countplot(x='sex', data=df_clean)
plt.title('Distribución por Sexo')
plt.show()

# Histograma para la variable 'age' (numérica)
df_clean['age'].plot(kind='hist', bins=20, edgecolor='black')
plt.title('Distribución de Edad')
plt.xlabel('Edad')
plt.show()

# Gráfico de cajas para la variable 'fare' según la 'pclass'
sns.boxplot(x='pclass', y='fare', data=df_clean)
plt.title('Tarifa por Clase de Boleto')
plt.xlabel('Clase')
plt.ylabel('Tarifa')
plt.show()
