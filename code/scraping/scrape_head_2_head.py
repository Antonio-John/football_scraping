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
home_team=config.get('team_info', 'hometeam')
away_team=config.get('team_info', 'awayteam')
head_2_head_url=config.get("url", "head_2_head")
CWD=config.get("directories", "head_2_head_dir")

# get html soup from website url
html_soup=ft.get_website(url=head_2_head_url)

# gets dataframe from the html soup
df_of_matches=ft.get_all_matches(soup=html_soup)

# save out dataframe
ft.save_csv(cwd=CWD,
            file=df_of_matches)




