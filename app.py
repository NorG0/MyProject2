import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px



st.title("HOẠT ĐỘNG LÀM VIỆC")
menu = ["Home","Login","SignUp"]
choice = st.sidebar.selectbox("Menu",menu)
task = st.selectbox("Task",["Dashboard","Profiles","Manage"])

