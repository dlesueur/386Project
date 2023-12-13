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


# team_df = games[games['home_team_name'] == team]
fig = px.histogram(team_scores_df, x='Scores', nbins=15, color_discrete_sequence=[teamColor1])
fig.update_xaxes(title_text = 'Score')
fig.update_yaxes(title_text = 'Frequency')
st.plotly_chart(fig, theme = None, use_container_width=True)


# fig, ax = plt.subplots()
# ax.hist(team_df['home_team_score'], bins=20, alpha=0.5, label="Home Team", color=teamColor1)  # Use your teamColor1
# ax.hist(team_df['visitor_team_score'], bins=20, alpha=0.5, label="Visitor Team", color=teamColor2)  # Use your teamColor2
# ax.legend()
# ax.set_xlabel('Points')
# ax.set_ylabel('Frequency')

# # Show the plot using Streamlit
# st.pyplot(fig)


st.text('Season Record Against Other Teams')
this_teams_list = teams['full_name']
this_team = st.selectbox('Select a team', this_teams_list, key = "selectbox2")
this_team_df = team_df[team_df['visitor_team_name'] == this_team]
scores = this_team_df[['date', 'home_team_score', 'visitor_team_score']].sort_values('date')
st.dataframe(scores)
