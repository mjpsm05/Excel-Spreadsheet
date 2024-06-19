import streamlit as st 
import pandas as pd 
import plotly.express as px 
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

st.title("Excel Spreadsheet Data")
st.header("By Mazamesso Meba")

df = pd.read_excel('/Users/mazamessomeba/Desktop/Projects/Excel/Excel_2.xlsx')


st.sidebar.header("Please Filer Here:")
Current_User_Queue = st.sidebar.multiselect(
    "Select User:",
    options=df["Current_User_Queue"].unique(),
    default=df["Current_User_Queue"].unique()
)


Assigned_Reviewer = st.sidebar.multiselect(
    "Select The Assigned Reviewer:",
    options=df["Assigned_Reviewer"].unique(),
    default=df["Assigned_Reviewer"].unique()
)

df_selection = df.query(
    "Current_User_Queue == @Current_User_Queue & Assigned_Reviewer == @Assigned_Reviewer"
)
st.dataframe(df_selection)


import datetime


d = st.date_input("What is Today's date", value=None)
st.write("Today's date is:", d)

df_map= pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [30.332184, -81.655647],
    columns=['lat', 'lon'])

st.map(df_map)
