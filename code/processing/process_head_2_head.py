from configparser import ConfigParser

# set ups directorys for imports
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import football_tools as ft

# current working directory
CWD = os.getcwd()

# Read in config file
config = ConfigParser()
config.read(os.path.join("code",'config.ini'))
team_1 = config.get('team_info', 'team_1')
team_2 = config.get('team_info', 'team_2')

# head to head
raw_dir = os.path.join(CWD,"data","head_2_head","raw")
teams = f"{team_1}v{team_2}"
head_2_head_path = os.path.join(raw_dir,teams)
df = ft.read_latest_excel(head_2_head_path)

# using cleaning functions
df_clean=ft.clean_and_derive(df=df)

# outputting the csv
path = os.path.join(CWD,"data", "head_2_head", "processed", f"{team_1}v{team_2}.csv")
df.to_csv(path)


