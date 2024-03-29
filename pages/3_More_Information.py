import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import matplotlib as plt



st.title("More Information")
st.markdown("This data was taken from the [Ball Don't Lie API](https://www.balldontlie.io/home.html#introduction).", unsafe_allow_html=True)
st.write("Team color information was taken from [Team Color Codes](https://teamcolorcodes.com/nba-team-color-codes/)")
st.write("For a demonstration of data collection, view my [blog post](https://dlesueur.github.io/Ball-Don't-Lie/) about the process I used to access this API.")
st.write("For more analysis of these graphs and a more thorough EDA, view this [blog post](https://dlesueur.github.io/EDA-Don't-Lie/)")
st.write("Here is my [repository](https://github.com/dlesueur/386Project) containing all of the code for this dashboard, as well as all of the code used to collet, clean, and explore this data.")

st.date_input("Starting Date:", format="YYYY-MM-DD", value=None)