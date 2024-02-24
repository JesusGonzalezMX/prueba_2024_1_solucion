import streamlit as st
import pandas as pd

# CArgamos la informacion
df = pd.read_csv('data/Procesamiento_salidas/razones_long.csv')

#separamos la columna del año para un mejor manejo de la informacion
df[['variable','anio']] = df['variable'].str.rsplit("_",n=1, expand=True)

# Now you can work with the DataFrame 'df'
print(df)