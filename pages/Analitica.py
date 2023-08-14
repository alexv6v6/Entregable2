import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
from matplotlib import pyplot as plt

st.set_page_config(page_title="EDA Demo", page_icon="📊")

# Importamos los datasets que vamos a utilizar.
folder = 'data'
archivo_data = 'tiempos.csv'
data = pd.read_csv(folder + '/' + archivo_data, sep=',')

# Definimos las clases que vamos a utilizar y reemplazamos su valor numérico con una inicial.
# Definir el diccionario de nombres de clases
nombre_clases = {
    1: "MANIZALES",
    2: "AGUADAS",
    3: "ANSERMA",
    4: "ARANZAZU",
    5: "BELALCAZAR",
    6: "CHINCHINA",
    7: "FILADELFIA",
    8: "LA DORADA",
    9: "LA MERCED",
    10: "MANZANARES",
    11: "MARMATO",
    12: "MARQUETALIA",
    13: "MARULANDA",
    14: "NEIRA",
    15: "NORCASIA",
    16: "PACORA",
    17: "PALESTINA",
    18: "PENSILVANIA",
    19: "RIOSUCIO",
    20: "RISARALDA",
    21: "SALAMINA",
    22: "SAMANÁ",
    23: "SAN JOSÉ",
    24: "SUPIA",
    25: "VICTORIA",
    26: "VILLAMARIA",
    27: "VITERBO"
}

# Definir el diccionario de clasificación de variables
clasificacion_variables = {
    1: "Concesión de agua subterránea",
    2: "Concesión de agua superficial",
    3: "Inscripción de Bosque",
    4: "Inscripción de Plantaciones",
    5: "Licencias ambientales",
    6: "Plan de manejo ambiental",
    7: "Permiso aprovechamiento forestal mayor bosque natural"
}


d = data.copy()
d['Municipio'] = d['Municipio'].replace(nombre_clases)
d['Tipo'] = d['Tipo'].replace(clasificacion_variables)


st.markdown("# Análisis Exploratorio de Datos (EDA)")
st.sidebar.header("EDA Demo")
st.write("Vamos a visualizar algunos aspectos de los datos.")

# Mostrar el DataFrame en Streamlit
st.write("## Vista previa del DataFrame")
st.dataframe(d.head())

# Realizar el conteo de las clases Municipio
conteo_municipio = d["Municipio"].value_counts()

# Realizar el conteo de las categorías Tipo
conteo_tipo = d["Tipo"].value_counts()

# Mostrar el conteo de clases Municipio en forma de tabla
st.write("## Conteo de Clases Municipio")
st.dataframe(conteo_municipio)

# Mostrar el conteo de categorías Tipo en forma de tabla
st.write("## Conteo de Categorías Tipo")
st.dataframe(conteo_tipo)

# Graficar el conteo de las categorías Tipo en un gráfico de torta (Plotly)
st.write("## Gráfico de Torta del Conteo de Categorías Tipo")
fig_tipo = px.pie(names=conteo_tipo.index, values=conteo_tipo.values)
st.plotly_chart(fig_tipo)



# Excluir los campos no numéricos
numeric_columns = ['tiempo1', 'tiempo2', 'tiempo3', 'tiempo4', 'tiempo5', 'tiempo6', 'tiempototal']

# Obtener el resumen estadístico
summary = data[numeric_columns].describe()

st.markdown("# Resumen Estadístico de Campos Numéricos")
st.sidebar.header("Exploración de Datos")
st.write("Bienvenido al resumen estadístico de campos numéricos.")

# Vista previa del DataFrame
st.write("## Vista previa del DataFrame")
st.dataframe(data[numeric_columns].head())

# Resumen estadístico de campos numéricos
st.write("## Resumen Estadístico de Campos Numéricos")
st.dataframe(summary)

