import pandas as pd
from configparser import ConfigParser
from football_tools import get_website

# Read in config file
config = ConfigParser()
config.read('config.ini')

# home and away team
home_team=config.get('team_info', 'hometeam')
away_team=config.get('team_info', 'awayteam')

url="https://www.11v11.com/teams/"+home_team+"/tab/opposingTeams/opposition/"+away_team
html_soup=get_wesbite(url)
print(html_soup)


