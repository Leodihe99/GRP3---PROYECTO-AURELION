import pandas as pd
import numpy as np
from pathlib import Path

# ruta relativa al script -> c:\Users\ileon\Downloads\GRP3 - Proyecto Aurelion\databases\ventas.xlsx
BASE = Path(__file__).parent
ventas_path = BASE / 'databases' / 'ventas.xlsx'

# leer archivo Excel (usa openpyxl)
df = pd.read_excel(ventas_path, engine='openpyxl')

print("Primeras filas del DataFrame:")
print(df.head())

print("\n")
print("Información del DataFrame:")
print(df.info())

print("\n")
print("Descripción cuantitativa del DataFrame:")
print(df.describe(include='number'))

print("\n")
print("Descripción de columnas categóricas:")
print(df.describe(include='object'))

print("\n")
print("Descripción de columnas datetime:")
print(df.describe(include='datetime'))

print("\n")
print("Valores nulos por columna:")
print(df.isnull().sum())

print("\n")
print("Número de filas duplicadas:")
print(df.duplicated().sum())

print("\n")
print("Valores atípicos por columna numérica:")
print("Usando el método del rango intercuartílico (IQR):")
print("-----------------------------------------")
for col in df.select_dtypes(include=[np.number]).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"{col}: {len(outliers)} outliers")

print("\n")
print("Rango estadistico de columnas numéricas:")
print("-----------------------------------------")
print(df.select_dtypes(include=[np.number]).agg(['min', 'max', 'mean', 'median', 'std']))

