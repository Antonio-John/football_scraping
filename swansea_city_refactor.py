# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 11:12:39 2021

@author: 44752
"""

import pandas as pd
from bs4 import BeautifulSoup as soup
import os
import urllib.request

url = "https://www.11v11.com/teams/swansea-city/tab/matches/season/2020/"

def get_website(url):
    
    agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.277"
    r = urllib.request.Request(url, headers= {'User-Agent' : agent})
    html = urllib.request.urlopen(r)
    page_soup_test = soup(html, "html.parser")

    return page_soup_test

def get_containers_boxes(soup):
    
    containers_of_boxes = soup.findAll("tr")
    
    return containers_of_boxes

def get_info(box):
    
    match = box
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
        aggregate_score = "-"
    else:
        aggregate_score = "-"
        penalties = "-"
        
    score_list = score.split("-")
    home_goals = score_list[0]
    away_goals = score_list[1]

    comp = info[4].text.strip()
    
    
    return (date, teams, home_team, away_team, opposition, result, 
            score, home_goals,  away_goals, aggregate_score,  penalties,  comp)


if __name__ == "__main__":
    
    f = open("swanseacitymatches.csv", "w", errors="ignore")
    
    seasons = list(range(1945,2021))
    seasons = [str(i) for i in seasons]
    
    f.write("Date" + "," + "Teams" + "," + "Home_team" "," + "Away_team" + "," 
            "Opposition" + "," + "Result" + "," + "Score" + "," + "Home_goals" 
            + "," + "Away_goals" 
            + "," + "Aggregrate_score" + "," + "Peanalties" + "," + "Competition" + 
            "," + "Season" + "\n")
    
    for season in seasons:
        url="https://www.11v11.com/teams/swansea-city/tab/matches/season/"+season+"/"
        website=get_website(url)
        matches=get_containers_boxes(website)
        
        for match in range(1, len(matches)):
            info=get_info(matches[match])
            
            f.write(info[0] + "," + info[1]  + "," + info[2]  + "," + info[3]   + 
                        "," + info[4]  + ","+ info[5]  + "," 
                        + info[6]  + "," + info[7]  + "," + info[8]  + "," + 
                        info[9]  + "," + info[10]  + "," + info[11]  + "," + str(int(season)-1) + "\n")
    
    f.close()
        
        
    
    
    






