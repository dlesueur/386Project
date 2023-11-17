import requests
import pandas as pd

games_url = "https://www.balldontlie.io/api/v1/games"
games_list = []
def get_page_game(number):
    para = {"page" : number , "per_page" : 100, "seasons[]" : [2022]}
    r = requests.get(games_url, params = para)
    r.status_code
    data = r.json()
    games_df = pd.DataFrame(data['data'])
    games_df['home_team_id'] = games_df['home_team'].apply(lambda x: x.get('id') if isinstance(x, dict) else None)
    games_df['visitor_team_id'] = games_df['visitor_team'].apply(lambda x: x.get('id') if isinstance(x, dict) else None)
    games_df = games_df.drop(['home_team', 'visitor_team'], axis=1)
    games_list.append(games_df)
for i in range(0, 15):
    get_page_game(i)