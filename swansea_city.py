# packages needed
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def swansea_process():
    # getting the data 
    os.chdir('C:\\webscraping')
    
    
    # list to get all the seasons
    seasons = list(range(1945,2021))
    seasons = [str(i) for i in seasons]
    
    
    # creating the file
    
    filname = "Swansea_city_"+datetime.now().strftime("%m/%d/%Y")+"_.csv"
    
    f = open(filname, "w")
    
    f.write("Date" + "," + "Teams" + "," + "Home_team" "," + "Away_team" + "," 
            "Opposition" + "," + "Result" + "," + "Score" + "," + "Home_goals" 
            + "," + "Away_goals" 
            + "," + "Aggregrate_score" + "," + "Peanalties" + "," + "Competition" + 
            "," + "Season" + "\n")
    
    for season in seasons:
        
        # this reads in the website using the beautiful soup package
        url = "https://www.11v11.com/teams/swansea-city/tab/matches/season/"+season+"/"
        uClient_test = uReq(url)
        page_html_test = uClient_test.read()
        page_soup_test = soup(page_html_test, "html.parser")
        
        containers_of_boxes = page_soup_test.findAll("tr")
        
        for i in range(1,len(containers_of_boxes)):
            print(i)
            
            match = containers_of_boxes[i]
            info = match.findAll("td")
            date = info[0].text.strip()
            teams = info[1].text.strip()
            team_list = teams.split(" v ")
            
            home_team = team_list[0].strip()
            away_team = team_list[1].strip()
            
            if home_team == "Swansea Town" or home_team == "Swansea City":
                opposition = away_team
            else:
                opposition = home_team
            
            result = info[2].text.strip()
            
            score = str(info[3].text.strip())
            if "Agg" in score:
                score_list = score.split("Agg:")
                score = score_list[0]
                aggregate_score = score_list[1]
                penalties = "-"
            elif "(" in score:
                score_list = score.split("(")
                score = score_list[0]
                penalties = score_list[0]
                penalties = penalties.strip(")")
            else:
                aggregate_score = "-"
                penalties = "-"
                
            score_list = score.split("-")
            home_goals = score_list[0]
            away_goals = score_list[1]
        
            comp = info[4].text.strip()
        
            f.write(date + "," + teams + "," + home_team + "," + away_team  + 
                    "," + opposition + ","+ result + "," 
                    + score + "," + home_goals + "," + away_goals + "," + 
                    aggregate_score + "," + penalties + "," + comp + "," + str(int(season)-1) + "\n")
            
    f.close()

    return()
    
swansea_process()
# 
# """
# Read in and transformations
# """
#     
# df = pd.read_csv("Swansea_city.csv")
# df["Year"] = df.Date.str[6:11]
# 
# df["Swansea_goal"]=""
# df["Opposition_goal"]=""
# 
# for i in range(len(df)):
#     if df["Home_team"][i] == "Swansea City" or df["Home_team"][i] == "Swansea Town":
#         df["Swansea_goal"][i] = df["Home_goals"][i]
#     else:
#         df["Opposition_goal"][i] = df["Home_goals"][i]
#         
#     if df["Away_team"][i] == "Swansea City" or df["Away_team"][i] == "Swansea Town":
#         df["Swansea_goal"][i] = df["Away_goals"][i]
#     else:
#         df["Opposition_goal"][i] = df["Away_goals"][i]
#   
# df.to_csv("Swansea_City"+datetime+".csv")
# 
# 
# # 151 teams played again
# teams = list(df["Home_team"].unique())
# alphabet_teams = sorted(teams)
# 
# """
# # times we played against each teach
# """
# by_team = df.groupby(["Opposition"]).count()
# 
# """
# Cardiff Anaylysis
# """
# 
# 
# cardiff_df = df[(df["Home_team"]=="Cardiff City") |
#                 (df["Away_team"]=="Cardiff City")]
# 
# cardiff_df_byseason = cardiff_df.groupby(["Season"]).count()
# cardiff_df_byseason_sorted = cardiff_df_byseason.sort_index()
# cardiff_df_byseason_sorted["Season"] = cardiff_df_byseason_sorted.index
# cardiff_df_byseason_sorted = cardiff_df_byseason_sorted[["Date","Season"]]
# cardiff_df_byseason_sorted_diff = cardiff_df_byseason_sorted.diff()
# 
# seasons = list(range(1945,2020))
# cardiff_seasons = list(cardiff_df_byseason.index)
# cardif_non_seasons = list(set(seasons) - set(cardiff_seasons))
# zero = [0] * len(cardif_non_seasons)
# cardiff_empty = pd.DataFrame(list(zip(cardif_non_seasons, zero)), 
#                              columns=["Season", "Date"])
# 
# cardiff = pd.concat([cardiff_df_byseason_sorted,cardiff_empty])
# cardiff_sorted = cardiff.sort_values(by=["Season"])
# 
# cardiff_plt = plt.bar(cardiff_sorted["Season"], cardiff_sorted["Date"])
# plt.xlabel("Seasons")
# plt.ylabel("Games")
# plt.title("Swans vs Cardiff over the years")
# dir(plt)
# 
# 
# """
# Success against teams
# """
# 
# by_team_goals = df.groupby(["Opposition"]).sum()
# del(by_team_goals["Season"])
# by_team_goals["Total"] = by_team_goals["Home_goals"]  + by_team_goals["Away_goals"] 
# 
# # goals per team
# by_team_goal_per_game = df.groupby(["Opposition"]).mean()
# 
# df["total_goals"] = df["Home_goals"] + df["Away_goals"]
# by_result = df.groupby(["Result"]).count()
# 
# teams = list(df["Home_team"].unique())
# 
# 
# # by compeitition
# 
# by_competition = df.groupby(["Competition"]).count()
# =============================================================================

# 3-1
# 2-2






