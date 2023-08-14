import streamlit as st
import requests
import pandas as pd


st.set_page_config(page_title="Predicción de Tiempos", page_icon="⏱️")

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

def solicitud_API(muestra: list):
    # URL de la API
    url = "https://apientregable2.azurewebsites.net/predict/"

    # Datos que serán enviados en el cuerpo de la petición
    data = {
        "municipio": int(muestra[0]),
        "tipo": int(muestra[1])
    }

    # Realizar la petición POST a la API
    response = requests.post(url, json=data)

    # Verificar si la petición fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener la respuesta en formato JSON
        result = response.json()

        return result
    else:
        return None

st.subheader("Características de entrada")
features = ['Municipio', 'Tipo']

st.write("A continuación, seleccione los valores de las características que serán utilizadas para la predicción de tiempos a partir del modelo de Machine Learning:")

def user_input_parameters():
    inputs = {}
    for feature in features:
        if feature == 'Municipio':
            selected_municipio = st.selectbox(f"Seleccione {feature}", list(nombre_clases.values()))
            selected_municipio_codigo = list(nombre_clases.keys())[list(nombre_clases.values()).index(selected_municipio)]
            inputs[feature] = selected_municipio_codigo
        elif feature == 'Tipo':
            selected_tipo = st.selectbox(f"Seleccione {feature}", list(clasificacion_variables.values()))
            selected_tipo_codigo = list(clasificacion_variables.keys())[list(clasificacion_variables.values()).index(selected_tipo)]
            inputs[feature] = selected_tipo_codigo
    return inputs

df = user_input_parameters()

st.markdown("# Predicción de Tiempos")
st.sidebar.header("Predicción de Tiempos")
st.write("Ingrese los valores de las características para predecir los tiempos:")

# Mostrar el DataFrame en Streamlit
st.write("## Características de Entrada")
st.table(pd.DataFrame(df, index=[0]))

# Crear un botón 'PREDECIR'
predict_button = st.button('PREDECIR')
prediction_result = None

if predict_button:
    # Validar que todos los campos contengan valores numéricos
    all_numeric = all(isinstance(value, int) for value in df.values())

    if not all_numeric:
        st.warning("Por favor, complete todos los datos con valores numéricos antes de hacer la predicción.")
    else:
        # Realizar la predicción usando la función de solicitud_API
        prediction_result = solicitud_API(list(df.values()))

        if prediction_result is not None:
            if "Tiempo Total" in prediction_result:
                st.success("Resultados de predicción:")
                for key, value in prediction_result.items():
                    st.write(f"{key}: {value}")
            else:
                st.error("La respuesta de la API no contiene los resultados esperados.")
        else:
            st.error("No se obtuvo una respuesta válida desde la API.")


