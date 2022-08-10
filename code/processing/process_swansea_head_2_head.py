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
away_team=config.get('team_info', 'awayteam')
CWD=config.get("directories", "head_2_head_dir")

df=ft.read_latest_excel(os.path.join(CWD+away_team))


# clean data/add extra variables
df_clean=ft.change_team_names(df=df,
                             old_name="Swansea Town",
                             new_name="Swansea City")

# clean and drive the dataframe
df_clean=ft.clean_and_derive(df=df_clean)

#TODO Lookup file 
# dates for month, years etc
# save out 
