from operator import index
import urllib.request
from bs4 import BeautifulSoup as soup
import pandas as pd
import os
from configparser import ConfigParser

CWD =  os.path.join(os.getcwd(), "football_scraping")

def load_config(): 

    config = ConfigParser()
    config.read(os.path.join(CWD,
                            "code",
                            "config.ini"))
    return config

# load config file
config = load_config()

TEAM1 = config.get('team_info', 'team_1')
TEAM2 = config.get('team_info', 'team_2')

def get_website(url):
    """
    scrapes html page for website
    """
    agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.277"
    r = urllib.request.Request(url, headers= {'User-Agent' : agent})
    html = urllib.request.urlopen(r)
    page_soup_test = soup(html, "html.parser")

    return page_soup_test

def get_all_matches(soup):
    """
    get's all the matches from the table
    """
    # set up dataframe
    df=pd.DataFrame({"date":[],
                     "match":[],
                     "result":[],
                     "score":[],
                     "competition":[]})

    # get big table of matches
    big_table=soup.findAll("tbody")[0]
    matches=big_table.findAll("tr")

    # iterate though all matches and append to data
    for i in range(len(matches)-1):
        one_match=matches[i]
        entries=one_match.findAll("td")
        date=entries[0].text
        link=entries[1].text
        result=entries[2].text
        score=entries[3].text
        competition=entries[4].text

        df.loc[len(df)] = [date,link,result,score,competition]

    return df

def save_csv(cwd, file, teams):
    """
    given cwd and file will save the file
    with the name of the teams
    """

    # gets name of match to call it the file this
    (team1, team2) = teams

    # file name
    file_name = os.path.join(cwd,f"{team1}v{team2}.csv")
    file.to_csv(file_name,
                index=False)

def read_latest_excel(cwd):
    """
    reads in latest file 
    """
    # lists files and get's the latest one
    files=os.listdir(cwd)
    wanted=[file for file in files if file.endswith(".csv")]
    wanted_with_path=[cwd+"/"+file for file in wanted]
    latest_file = max(wanted_with_path, key=os.path.getctime)

    # use pandas to read in
    df=pd.read_csv(latest_file)

    return df


def change_team_names(df, old_name, new_name):
    """
    changes old team name to new name
    e.g Swansea Town to Swansea City

    """
    for col in df.columns:
        if type(col) == str:
            df[col] = df[col].str.replace(old_name, new_name)
   

    return df

def split_home_away(df):

    df['home_team'] = df['match'].str.split(' v ', expand=True)[1]
    df['away_team'] = df['match'].str.split(' v ', expand=True)[0]

    df["home_goals"]=df["score"].str.split("-", expand=True)[0]
    df["away_goals"]=df["score"].str.split("-", expand=True)[1]

    return df

def clean_and_derive(df):

    df=split_home_away(df)

    return df

def format_team_2_nm_for_scraping(team_name:str):

    team_name_adjusted = team_name.replace(" ", "%20")

    return team_name_adjusted


def format_team_1_nm_for_scraping(team_name:str):

    team_lower = team_name.lower()
    team_name_adjusted = team_lower.replace(" ", "-")

    return team_name_adjusted