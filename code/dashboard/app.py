# https://docs.streamlit.io/library/cheatsheethttps://docs.streamlit.io/library/cheatsheet
# https://docs.streamlit.io/library/advanced-features/session-state

import os

import streamlit as st
import pandas as pd
import numpy as np 

import app_tools as app


# reading in the data
df = pd.read_csv(os.path.join("data",
                            "transformed",
                            "swanseacitymatches.csv"))

#title 
st.title('Swansea City Match Statistics')
# header 
st.header('About')

# description
st.write("Welcome to a page dedicated to Swansea City Statistics.")

# sidebar with select box
add_selectbox = st.sidebar.selectbox(
    "This is just a placeholder",
    ("option a", "option b", "option c")
)

st.image(image="swansea_image.jpg",
caption="Wherever Swansea City go, the north bank goes aswell")

# this is a container
c = st.container()
c.write("Top of cotainer")

# chart 
df_home_team = df[["away_goals","home_goals"]]

# needs editing 
st.bar_chart(data=df_home_team)

# information message
#st.info('This is a purely informational message')
