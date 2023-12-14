import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import matplotlib as plt

st.title('2022-23 NBA Season')

teams = pd.read_csv('datasets/teams.csv')
teams_list = teams['full_name']
team = st.selectbox('Select a team', teams_list, key = "selectbox1")


st.text('Distribution Of Points Scored')

games = pd.read_csv('datasets/games.csv')
colors = pd.read_csv('datasets/teamColors.csv')
teamColor1 = colors.loc[colors['full_name'] == team, 'colorHex'].values[0]
teamColor2 = colors.loc[colors['full_name'] == team, 'ColorHex2'].values[0]
home_scores = games[games['home_team_name'] == team]['home_team_score']
visitor_scores = games[games['visitor_team_name'] == team]['visitor_team_score']
team_scores = []
team_scores.extend(home_scores)
team_scores.extend(visitor_scores)
team_scores_df = pd.DataFrame(team_scores, columns=['Scores'])
fig = px.histogram(team_scores_df, x='Scores', nbins=15, color_discrete_sequence=[teamColor1])
fig.update_xaxes(title_text = 'Score')
fig.update_yaxes(title_text = 'Frequency')
st.plotly_chart(fig, theme = None, use_container_width=True)


st.title("Recorded Player Heights")
players = pd.read_csv('datasets/playersCurrent.csv')
playersWithHeight = players[players['height'] != 0]
team_id = teams.loc[teams['full_name'] == team, 'id'].values[0]
teamsPlayers = playersWithHeight[playersWithHeight['team_id'] == team_id]
fig2 = px.histogram(teamsPlayers, x='height', nbins = 15, color_discrete_sequence=[teamColor2])
fig2.update_xaxes(title_text = 'Height')
fig2.update_yaxes(title_text = 'Frequency')
st.plotly_chart(fig2, theme = None)

# POINTS SCORED VS OPPONENT SCATTERPLOT


# st.text('Season Record Against Other Teams')
# this_teams_list = teams['full_name']
# this_team = st.selectbox('Select a team', this_teams_list, key = "selectbox2")
# this_team_df = team_df[team_df['visitor_team_name'] == this_team]
# scores = this_team_df[['date', 'home_team_score', 'visitor_team_score']].sort_values('date')
# st.dataframe(scores)
