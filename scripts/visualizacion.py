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
     df.drop(df[df['tipo_combustible'] == 'Total'].index, inplace=True)
     convert_dict = {'modo_transporte': str,
                     'tipo_combustible': str,
                     'valor': float,
                     'anio': int
                    }
 
     df = df.astype(convert_dict)
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
de gasolina y dísel.
""")

st.markdown("""
Para este fin se usara la salida del script de procesamiento, 
en especifico el archivo en formato long "/data/Procesamiento_salidas/razones_long.csv"
""")

#separamos la columna del año para un mejor manejo de la informacion
st.write(df.head())


st.header('Evolucion del consumo domestico por modo de transporte')
groupedvalues = df.groupby(['modo_transporte','anio']).sum().reset_index()
groupedvalues.drop(groupedvalues[groupedvalues['modo_transporte'].isin(['HIGHWAY ','NONHIGHWAY'])==True].index, inplace=True)
fig = plt.figure(figsize=(10, 4))
sns.barplot(data=groupedvalues, y='valor', x='anio', hue='modo_transporte')
st.pyplot(fig)
st.markdown("""
En la grafica anterior podemos observar que el uso de combustibles por modo de 
transporte ha mantenido la proporcion a lo largo de los años, sin embargo se ha reducido 
al rededor del 50% para los vehiculos ligeros y medianos, que son los que consumen una 
mayor cantidad de comnbustible.
""")

st.header('Evolucion del consumo domestico por tipo de combustible')
groupedvalues = df.groupby(['tipo_combustible','anio']).sum().reset_index()
fig = plt.figure(figsize=(10, 4))
sns.barplot(data=groupedvalues, y='valor', x='anio', hue='tipo_combustible')
st.pyplot(fig)
st.markdown("""
En la grafica anterior podemos observar que el uso de combustibles segun su tipo
ha mantenido la proporcion a lo largo de los años, salvo el consumo de gas natural,
el cual se ha reducido muchisimo.
""")

st.header('Cambios en las proporciones de consumo de gasolina y dísel')
groupedvalues = df.groupby(['tipo_combustible','anio']).sum().reset_index()
groupedvalues.drop(groupedvalues[groupedvalues['tipo_combustible'].isin(['Gasoline','Diesel_fuel'])==False].index, inplace=True)
fig = plt.figure(figsize=(10, 4))
sns.barplot(data=groupedvalues, y='valor', x='anio', hue='tipo_combustible')
st.pyplot(fig)
st.markdown("""
En la grafica anterior podemos observar que aunque de manera lenta, existe una ligeria tendencia 
a usar mas disel y menos gasolina.
""")

