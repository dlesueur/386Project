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
players_current = pd.read_csv("datasets/playersCurrent.csv")

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
team_stats['team_id'] = range(1, 31)
team_stats = team_stats.merge(teams[['full_name', 'id']], left_on = 'team_id', right_on = 'id')

st.text('Average Points Per Game vs. Win Percentage')
fig = px.scatter(team_stats, x = 'average_points', y = 'win_pct', color='full_name', color_discrete_sequence= ['#a4c2a5'])
fig.update_layout(
    xaxis_title='Average Points Per Game',
    yaxis_title='Win Percentage'
)
fig.update_traces(showlegend=False)
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
fig2 = px.scatter(team_stats, x = 'opponent_avg_points', y = 'win_pct', color = 'full_name', color_discrete_sequence= ['#28536b'])
fig2.update_layout(
    xaxis_title='Average Opponents\' Points Per Game',
    yaxis_title='Win Percentage'
)
fig2.update_traces(showlegend=False)
st.plotly_chart(fig2, theme = None)

st.text('Average Points Per Game vs. Average Opponents\'s Points Per Game')
fig3 = px.scatter(team_stats, x = 'average_points', y = 'opponent_avg_points', color = 'full_name', color_discrete_sequence = ['#984447'])
fig3.update_layout(
    xaxis_title='Average Points Per Game',
    yaxis_title='Average Opponents\' Points Per Game'
)
fig3.update_traces(showlegend=False)
st.plotly_chart(fig3, theme = None)


new_stats = stats[stats['min'] != 0 ]
player_points = new_stats.groupby('player_id').agg(
    average_points = pd.NamedAgg(column = 'pts', aggfunc='mean'),
    average_made = pd.NamedAgg(column = 'fg_pct', aggfunc = 'mean'),
    average_3_made = pd.NamedAgg(column = 'fg3_pct', aggfunc = 'mean')
)

player_points = player_points.merge(players_current[['id', 'height', 'name']], left_on = 'player_id', right_on = 'id', how = 'left')
player_points.drop(columns = ['id'], axis = 1, inplace=True)
player_points.dropna(inplace=True)
player_points['height'] = player_points['height'].astype('int')

st.text('Height vs. Points')

fig4 = px.scatter(player_points, x = 'height', y = 'average_points', color = 'name', color_discrete_sequence = ['#EF8354'])
fig4.update_layout(
    xaxis_title='Height (inches)',
    yaxis_title='Average Points Per Game'
)
fig4.update_traces(showlegend=False)
st.plotly_chart(fig4, theme = None)

st.text('Height vs. Avg FG Made')
fig5 = px.scatter(player_points, x = 'height', y = 'average_made', color = 'name', color_discrete_sequence= ['#a4c2a5'])
fig5.update_layout(
    xaxis_title='Height (inches)',
    yaxis_title='Average FG Rate Per Game'
)
fig5.update_traces(showlegend=False)
st.plotly_chart(fig5, theme = None)





st.text('Height vs. Avg 3 Point Shot Made')

fig6 = px.scatter(player_points, x = 'height', y = 'average_3_made', color = 'name', color_discrete_sequence = ['#984447'])
fig6.update_layout(
    xaxis_title='Height (inches)',
    yaxis_title='Average 3 Point Shot Made Per Game'
)
fig6.update_traces(showlegend=False)
st.plotly_chart(fig6, theme = None)


stats_small = stats[['player_id', 'reb', 'pts', 'fg3m', 'fgm', 'min', 'blk']]
stats_small = stats_small.merge(players_current[['id', 'height', 'name']], left_on = 'player_id', right_on = 'id')
stats_small.drop(columns = 'id', axis = 1, inplace = True)
stats_small = stats_small[stats_small['min'] != 0]

fig7 = px.scatter(stats_small, x = 'height', y = 'reb', color = 'name', color_discrete_sequence = ['#EF8354'])
fig7.update_layout(
    xaxis_title='Height (inches)',
    yaxis_title='Rebounds'
)
fig7.update_traces(showlegend=False)
st.plotly_chart(fig7, theme = None)



fig8 = px.scatter(stats_small, x = 'height', y = 'blk', color = 'name', color_discrete_sequence= ['#a4c2a5'])
fig8.update_layout(
    xaxis_title='Height (inches)',
    yaxis_title='Blocks'
)
fig8.update_traces(showlegend=False)
st.plotly_chart(fig8, theme = None)



