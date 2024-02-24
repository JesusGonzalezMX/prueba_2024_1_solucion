import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

#Loading the data
@st.cache_resource
def get_data():
     df = pd.read_csv('data/Procesamiento_salidas/razones_long.csv').fillna('0')
     df[['tipo_combustible','anio']] = df['tipo_combustible'].str.rsplit("_",n=1, expand=True)
     convert_dict = {'modo_transporte': str,
                     'tipo_combustible': str,
                     'valor': float,
                     'anio': int
                    }
 
     df = df.astype(convert_dict)
     print(df.info())
     return df

#configuration of the page
st.set_page_config(layout="wide")
#load dataframes
df = get_data()



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

#separamos la columna del año para un mejor manejo de la informacion
st.write(df)


st.header('Chart')
groupedvalues = df.groupby(['modo_transporte','anio']).sum().reset_index()
st.write(groupedvalues)
fig = plt.figure(figsize=(10, 4))
sns.barplot(data=groupedvalues, y='valor', x='anio', hue='modo_transporte')
st.pyplot(fig)