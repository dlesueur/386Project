import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

st.title('2022-23 NBA Season')

st.text('Distribution Of Points When At Home')

df = pd.read_csv('games.csv')
teams = pd.read_csv('teams')
teams_list = teams['full_name']
team = st.selectbox('Select a team', teams_list)

team_df = df[df['home_team_name'] == team]
fig = px.histogram(team_df, x='home_team_score', nbins=20, title='Score Distribution When Playing At Home')
fig.update_xaxes(title_text = 'Score')
fig.update_yaxes(title_text = 'Frequency')
st.plotly_chart(fig)


