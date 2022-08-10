# core imports

# third party imports
import pandas as pd

# modules imports
from .. import football_tools

def transform_data(df_name):

    # look through this logic s
    df = pd.read_csv(df_name, sep=",")
        
    df["year"] = pd.DatetimeIndex(df["date"]).year
    df["month"] = pd.DatetimeIndex(df["date"]).month
    df["day"] = pd.DatetimeIndex(df["date"]).day
    
    df=df.replace(to_replace="Swansea Town",value="Swansea City")
    
    cols_change_town_city=["date",'teams', 'home_team', 'away_team', 'opposition']
    
    for col in cols_change_town_city:
        df[col]=df[col].replace({"Swansea Town":"Swansea City"}, regex=True)
    
    conditions=[df["home_team"]=="Swansea City",df["away_team"]=="Swansea City"]
    choices=[df["home_goals"],df["away_goals"]]
    df["swansea_goal"]=np.select(conditions, choices)
    
    conditions=[df["home_team"]!="Swansea City",df["away_team"]!="Swansea City"]
    choices=[df["home_goals"],df["away_goals"]]
    df["opposition_goals"]=np.select(conditions, choices)
    
    return df

if __name__ == "__main__":

    file_name = "data/raw/swanseacitymatches.txt"
    transformed_df=transform_data(file_name)

    # save out clean file
    transformed_df.to_csv("data/transformed/swanseacitymatches.csv")