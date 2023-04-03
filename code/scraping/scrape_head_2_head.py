# core imports 
from configparser import ConfigParser

# set ups directorys for imports
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import football_tools as ft

# load config
config = ft.load_config()

# get info from config
team_1 = config.get('team_info', 'team_1')
team_2 =config.get('team_info', 'team_2')
head_2_head_url_dir = config.get("url", "head_2_head")

# swansea-city/tab/opposingTeams/opposition/

# get team names in right format to scrape 
team_1_name_for_url = ft.format_team_1_nm_for_scraping(team_1)
team_2_name_for_url = ft.format_team_2_nm_for_scraping(team_2)

# dir url + specific team name
url_head_head = head_2_head_url_dir + team_1_name_for_url + \
             "/tab/opposingTeams/opposition/" + team_2_name_for_url

# get html soup from website url
html_soup = ft.get_website(url=url_head_head)

# gets dataframe from the html soup
df_of_matches = ft.get_all_matches(soup=html_soup)

# output path 
raw_dir = os.path.join(ft.CWD,"data","head_2_head","raw")
principal_team = os.path.join(raw_dir,team_1+"v"+team_2)

if not os.path.exists(principal_team):
    os.mkdir(principal_team)

# save out dataframe
ft.save_csv(cwd=principal_team,
            file=df_of_matches,
            teams=(team_1, team_2))




