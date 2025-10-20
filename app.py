import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
# hist_button = st.button('Construir histograma')  # crear un botón

# if hist_button:  # al hacer clic en el botón
# escribir un mensaje
#   st.write(
# 'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

st.header("Proyecto Sprit 7: Visualización de datos de anuncios de venta de coches")

st.header("")

st.markdown(
    "<h1 style='font-size:20px;'>Histograma de automóviles según su odómetro</h1>",
    unsafe_allow_html=True
)

build_histogram = st.checkbox('Construir un histograma')
if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('haz  seleccionado la casilla para generar un grafico de histograma. ahora vamos a construirlo para la columna odometro')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


st.markdown(
    "<h1 style='font-size:20px;'>Odometro vs Precio</h1>",
    unsafe_allow_html=True
)

build_scatter_odometer_vs_price = st.checkbox(
    'Construir un grafico de dispercion odometro vs precio')
if build_scatter_odometer_vs_price:  # si la casilla de verificación está seleccionada
    st.write('haz  seleccionado la casilla para generar un grafico de dispersión. ahora vamos a construirlo para la columna odometro vs precio')
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
   # fig.show()  # crear gráfico de dispersión

 # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

    # Analisis de automoviles marca Toyota en venta

# agrupamos por modelo contiene a toyota
grouped_data = car_data[car_data["model"].str.contains(
    "toyota", case=False, na=False)].groupby("model").size().reset_index(name='counts')


st.markdown(
    "<h1 style='font-size:20px;'>Automoviles TOYOTA en venta</h1>",
    unsafe_allow_html=True
)


build_scatter_toyota_for_sale = st.checkbox(
    'Construir un grafico de barras de modelos de Toyota en venta')
if build_scatter_toyota_for_sale:  # si la casilla de verificación está seleccionada
    st.write('haz  seleccionado la casilla para generar un grafico de barras. ahora vamos a construirlo para los modelos de Toyota en venta')
    # crear un gráfico de barras
    fig = px.bar(grouped_data, x="model", y="counts")
   # fig.show()  # crear gráfico de barras

 # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# car_data = pd.read_csv(
#   'C:\\Users\\edson\\AppData\\Local\\Programs\\Python\\Python313\\Python_Edson\\TripleTen\\Sprint_7\\Project_Sprit_7\\vehicles_us.csv')
#  # leer los datos
# print(car_data.columns)


# crear una casilla de verificación
# build_histogram = st.checkbox('Construir un histograma')

# if build_histogram: # si la casilla de verificación está seleccionada
#    st.write('Construir un histograma para la columna odómetro')
