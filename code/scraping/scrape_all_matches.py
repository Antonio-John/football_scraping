# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 11:12:39 2021

@author: 44752
"""
from bs4 import BeautifulSoup as soup
import urllib.request
from configparser import ConfigParser

# set ups directorys for imports
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import football_tools as ft

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

    # read in config files
    config = ConfigParser()
    config.read(os.path.join("code",'config.ini'))
    
    # set up file path to save to
    file_name = os.path.join("data",'raw',"swanseacitymatches.txt")
    #file_name = "data/raw/swanseacitymatches.txt"
    f = open(file_name, "w", errors="ignore")
    
    # set up seasons want to get data for
    start_season = int(config.get("seasons", "start"))
    end_season = int(config.get("seasons", "end"))
    seasons = list(range(start_season, end_season+1))
    seasons = [str(i) for i in seasons]
    
    # write in column headers 
    f.write("date" + "," + "teams" + "," + "home_team" "," + "away_team" + "," 
            "opposition" + "," + "result" + "," + "score" + "," + "home_goals" 
            + "," + "away_goals" 
            + "," + "aggregrate_score" + "," + "peanalties" + "," + "competition" + 
            "," + "season" + "\n")
    
    # scrape for each season
    for season in seasons:
        url="https://www.11v11.com/teams/swansea-city/tab/matches/season/"+season+"/"
        website=get_website(url)
        matches=get_containers_boxes(website)
        
        # get info for each match
        for match in range(1, len(matches)):
            info=get_info(matches[match])
            
            f.write(info[0] + "," + info[1]  + "," + info[2]  + "," + info[3]   + 
                        "," + info[4]  + ","+ info[5]  + "," 
                        + info[6]  + "," + info[7]  + "," + info[8]  + "," + 
                        info[9]  + "," + info[10]  + "," + info[11]  + "," + str(int(season)-1) + "\n")
    
    # close file
    f.close()
    



    
    
        
        
    
    
    






