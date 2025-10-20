
# 🚗 Proyecto Sprint 7: Visualización de Datos de Anuncios de Venta de Coches

Este proyecto es una aplicación interactiva construida con **Streamlit** y **Plotly**, diseñada para analizar y visualizar datos de anuncios de automóviles usados.  
Permite explorar relaciones entre variables como el **odómetro**, el **precio** y los **modelos de automóviles Toyota**, de forma dinámica y visual.

---

## 🧩 Tecnologías utilizadas

- **Python 3.x**
- **Pandas** – para la manipulación y análisis de datos.
- **Plotly Express** – para generar gráficos interactivos.
- **Streamlit** – para crear la interfaz web interactiva.

---

## 📊 Descripción del proyecto

El programa carga un dataset (`vehicles_us.csv`) con información sobre vehículos usados publicados en Estados Unidos, y permite al usuario visualizar distintos aspectos mediante controles interactivos (checkboxes).

Las visualizaciones disponibles incluyen:

1. **Histograma de automóviles según su odómetro**  
   Muestra la distribución del kilometraje de los vehículos.

2. **Dispersión Odómetro vs Precio**  
   Permite observar la relación entre el kilometraje y el precio de venta.

3. **Gráfico de barras: Modelos de Toyota en venta**  
   Representa la cantidad de autos Toyota listados por modelo.

4. **Gráfico de barras: Modelos de Toyota vs Precio promedio**  
   Muestra el precio promedio de venta (en USD) para cada modelo Toyota.

---

## 🗂️ Estructura del proyecto

project/
│
├── vehicles_us.csv # Dataset con la información de los vehículos
├── app.py # Código principal del proyecto (este archivo)
└── README.md # Documentación del proyecto


---



