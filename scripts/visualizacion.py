import streamlit as st
import pandas as pd
import matplotlib
from matplotlib.backends.backend_agg import RendererAgg

#Loading the data
@st.cache_resource
def get_data_deputies():
     return pd.read_csv('data/Procesamiento_salidas/razones_long.csv')

matplotlib.use("agg")
_lock = RendererAgg.lock

#configuration of the page
st.set_page_config(layout="wide")
#load dataframes
df = get_data_deputies()
#separamos la columna del año para un mejor manejo de la informacion
df[['variable','anio']] = df['variable'].str.rsplit("_",n=1, expand=True)


st.title("Visualización y análisis de la información")
#st.subheader("Subtitulo")
#st.text('Esta')
st.markdown("""
Esta app ayuda a visualizar y los cambios registrados en el consumo 
de combustible por cada tipo de transporte de 2008 a 2019. 
Particularmente analiza los cambios en las proporciones de consumo 
de gasolina y dísel.'
""")

st.markdown("""
Para este fin se usara la salida del script de procesamiento, 
en especifico el archivo en formato long "/data/Procesamiento_salidas/razones_long.csv"
""")

st.write(df)