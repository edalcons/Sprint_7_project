import tkinter
import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv(
    'C:\\Users\\edson\\AppData\\Local\\Programs\\Python\\Python313\\Python_Edson\\TripleTen\\Sprint_7\\Project_Sprit_7\\vehicles_us.csv')  # leer los datos
print(car_data.columns)
