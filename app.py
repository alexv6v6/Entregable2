import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Clasificador Tiempos",
    page_icon="🌏",
)

st.write("# Clasificador de Tiempos para tramites según Municipio y Tipo 🕰️")

st.sidebar.success("Seleccione un item")
st.markdown(
    """
    ## Descripción de la base de datos de tiempos de los tramites 

    Una base de datos sobre los tiempos de los pasos del proceso de un tramite

    | Sigla | Descripción |
    |-------|-------------|
    | Tiempo1    | Tiempo que se toma desde que un tramite llega hasta que se paga la factura que se le genera |
    | Tiempo2    | Tiempo desde el pago de la factura hasta que se inicia formalmente el trámite |
    | Tiempo3    | Tiempo desde que se inicia hasta que se asigna para visita tecnica |
    | Tiempo4    | Tiempo desde la visita hasta la presentacion del informe tecnico|
    | Tiempo5    | Tiempo desde el informe tecnico hasta la resolucion del tramite|
    | Tiempo6    | Tiempo desde la resolucion hasta la notificacion a los solicitantes|
    | TiempoTotal| Tiempo total desde el inicio hasta la finalizacion del tramite|

    La base de datos contiene el tiempo en dias que transcurre en cada etapa del proceso.
    Ademas se tiene la informacion del municipio y el tipo de tramite

    """
)



# Cargar la imagen desde el archivo
st.write("## Modelo CANVAS del proyecto")
image_path = 'data/CANVAS.jpg'  # Reemplaza esto con la ruta de tu imagen
image = Image.open(image_path)

# Mostrar la imagen en Streamlit
st.image(image, caption='Modelo CANVAS del proyecto', use_column_width=True)