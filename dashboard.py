import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import matplotlib as plt

st.title('2022-23 NBA Season')

st.text('Distribution Of Points When At Home')
teams = pd.read_csv('datasets/teams.csv')
teams_list = teams['full_name']
team = st.selectbox('Select a team', teams_list, key = "selectbox1")


df = pd.read_csv('datasets/games.csv')
colors = pd.read_csv('datasets/teamColors.csv')
team_df = df[df['home_team_name'] == team]
fig = px.histogram(team_df, x='home_team_score', nbins=20, color = 'team', color_discrete_map=colors)
fig.update_xaxes(title_text = 'Score')
fig.update_yaxes(title_text = 'Frequency')
st.plotly_chart(fig, theme = None)


st.text('Season Record Against Other Teams')
this_teams_list = teams['full_name']
this_team = st.selectbox('Select a team', this_teams_list, key = "selectbox2")
this_team_df = team_df[team_df['visitor_team_name'] == this_team]
scores = this_team_df[['date', 'home_team_score', 'visitor_team_score']].sort_values('date')
st.dataframe(scores)

