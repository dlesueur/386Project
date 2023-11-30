import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

st.title('2022-23 NBA Season')

st.text('Distribution of Points by Team When Home and Visitng')

df = pd.read_csv('games.csv')
teams = pd.read_csv('teams')
team = st.selectbox('Select a team', teams['full_name'])

team_df = df[df['home_team_name'] == team]
fig = px.histogram(team_df, x='home_team_score', nbins=20, title='Home Team Score Distribution')
st.plotly_chart(fig)


