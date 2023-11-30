import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

st.title('2022-23 NBA Season')

st.text('Distribution of Points by Team')

df = pd.read_csv('pointsPerGame.csv')
team = st.selectbox('Select a team', 'df['full name']')

