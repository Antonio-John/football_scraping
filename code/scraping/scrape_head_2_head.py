# core imports 
from configparser import ConfigParser

# set ups directorys for imports
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import football_tools as ft

# Read in config file
config = ConfigParser()
config.read(os.path.join("code",'config.ini'))

# config items needed
# TODO: Dynamically create link from teams
team_1 = config.get('team_info', 'team_1')
team_2 =config.get('team_info', 'team_2')
head_2_head_url_dir = config.get("url", "head_2_head")

# get url link to scrape with 
team_name_for_url = ft.format_team_nm_for_scraping(team_2)

# dir url + specific team name
url_head_head = os.path.join(head_2_head_url_dir, team_name_for_url)

# get html soup from website url
html_soup = ft.get_website(url=url_head_head)

# gets dataframe from the html soup
df_of_matches = ft.get_all_matches(soup=html_soup)

# output path 
head_2_head = config.get("directories", "head_2_head_dir")
raw_dir = os.path.join(head_2_head,"raw")
principal_team = os.path.join(raw_dir,team_1)

if not os.path.exists(principal_team):
    os.mkdir(principal_team)

# save out dataframe
ft.save_csv(cwd=principal_team,
            file=df_of_matches)




