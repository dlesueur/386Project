import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import matplotlib as plt

st.title('2022-23 NBA Season')

teams = pd.read_csv('datasets/teams.csv')
teams_list = teams['full_name']
team = st.selectbox('Select a team', teams_list, key = "selectbox1")


st.text('Distribution Of Points When At Home vs. Opponent')

df = pd.read_csv('datasets/games.csv')
colors = pd.read_csv('datasets/teamColors.csv')
teamColor1 = colors.loc[colors['full_name'] == team, 'colorHex'].values[0]
teamColor2 = colors.loc[colors['full_name'] == team, 'ColorHex2'].values[0]
team_df = df[df['home_team_name'] == team]
fig = px.histogram(team_df, x='home_team_score', nbins=15, color_discrete_sequence=[teamColor1])
fig.update_xaxes(title_text = 'Score')
fig.update_yaxes(title_text = 'Frequency')
fig2 = px.histogram(team_df, x='visitor_team_score', nbins=15, color_discrete_sequence=[teamColor2])
fig2.update_xaxes(title_text = 'Opponent Score')
fig2.update_yaxes(title_text = 'Frequency')
st.plotly_chart(fig, theme = None)
st.plotly_chart(fig2, theme=None)

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
