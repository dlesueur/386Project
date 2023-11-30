import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

st.title('2022-23 NBA Season')
teams = pd.read_csv('teams')
teams_list = teams['full_name']
team = st.selectbox('Select a team', teams_list)
st.text('Distribution Of Points When At Home')

df = pd.read_csv('games.csv')
team_df = df[df['home_team_name'] == team]
fig = px.histogram(team_df, x='home_team_score', nbins=20)
fig.update_xaxes(title_text = 'Score')
fig.update_yaxes(title_text = 'Frequency')
st.plotly_chart(fig)


st.text('Season Record Against Other Teams When At Home')

opponent = st.selectbox('Select an opposing team', teams_list)

scores = team_df[['date', 'visitor_team_name', 'home_team_score', 'visitor_team_score']].sort_values('date')
st.dataframe(scores)

