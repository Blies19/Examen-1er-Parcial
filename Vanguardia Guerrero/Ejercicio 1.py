from sklearn.datasets import fetch_openml
import pandas as pd

# Descargar la base de datos Titanic
titanic = fetch_openml('titanic', version=1, as_frame=True)

# Extraer el dataframe
df = titanic.frame

# Mostrar la descripción de las primeras filas del dataset
print(df.head())

# Identificar el tipo de cada variable
print("\nTipos de variables:")
print(df.dtypes)
