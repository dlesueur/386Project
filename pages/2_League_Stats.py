import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import matplotlib as plt


st.title('2022-23 NBA Season League Stats')

games = pd.read_csv("datasets/games.csv")
players = pd.read_csv("datasets/players.csv")
stats = pd.read_csv("datasets/stats.csv")
teams = pd.read_csv("datasets/teams.csv")

home_team_stats = games.groupby('home_team_abr').agg(
    total_points=pd.NamedAgg(column='home_team_score', aggfunc='sum'),
    total_games=pd.NamedAgg(column='home_team_score', aggfunc='count')
)
visitor_team_stats = games.groupby('visitor_team_abr').agg(
    total_points=pd.NamedAgg(column='visitor_team_score', aggfunc='sum'),
    total_games=pd.NamedAgg(column='visitor_team_score', aggfunc='count')
)
team_stats = home_team_stats.add(visitor_team_stats, fill_value=0)
team_stats['average_points'] = team_stats['total_points'] / team_stats['total_games']
team_stats.sort_values('average_points', ascending=False)
team_stats.rename_axis('team', inplace=True)

team_stats['wins'] = 0
team_stats['losses'] = 0

for index, row in games.iterrows():
    home_team = row['home_team_abr']
    visitor_team = row['visitor_team_abr']
    home_score = row['home_team_score']
    visitor_score = row['visitor_team_score']
    
    # Update win/loss count based on scores
    if home_score > visitor_score:
        team_stats.loc[home_team, 'wins'] += 1
        team_stats.loc[visitor_team, 'losses'] += 1
    else:
        team_stats.loc[home_team, 'losses'] += 1
        team_stats.loc[visitor_team, 'wins'] += 1

team_stats['win_pct'] = team_stats['wins'] / team_stats['total_games']


st.text('Average Points Per Game vs. Win Percentage')
fig = px.scatter(team_stats, x = 'average_points', y = 'win_pct', color='team', color_discrete_sequence= ['#a4c2a5'])
fig.update_layout(
    xaxis_title='Average Points Per Game',
    yaxis_title='Win Percentage'
)
st.plotly_chart(fig, theme = None)


home_op_points = games.groupby('visitor_team_abr').agg(
    total_points = pd.NamedAgg(column='home_team_score', aggfunc='sum')
)
visiting_op_points = games.groupby('home_team_abr').agg(
    total_points = pd.NamedAgg(column='visitor_team_score', aggfunc = 'sum')
)
op_stats = home_op_points.add(visiting_op_points, fill_value=0)
team_stats['opponent_total_points'] = op_stats

team_stats['opponent_avg_points'] = team_stats['opponent_total_points'] / team_stats['total_games']

st.text('Average Opponents\' Points Per Game vs. Win Percentage')
fig2 = px.scatter(team_stats, x = 'opponent_avg_points', y = 'win_pct', colo = 'team', color_discrete_sequence= ['#28536b'])
fig2.update_layout(
    xaxis_title='Average Opponents\' Points Per Game',
    yaxis_title='Win Percentage'
)
st.plotly_chart(fig2, theme = None)

# plt.scatter(team_stats['opponent_avg_points'], team_stats['win_pct'], color = "red")
# plt.xlabel('Average Opponents Points Per Game')
# plt.ylabel('Win Percentage')
# plt.title('Average Opponent\'s Points Per Game vs. Win Percentage')
# plt.show()
