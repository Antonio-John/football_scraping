# Football Results Analysis

## Aims

The aims of this repository is to create analysis of football results & clubs. Initally starting with Swansea City, then generalising this code. The analysis is formed into two seperate parts.
1) Head to head results e.g Swansea City vs Newport County.
2) Every result of a club post 1945.

## Data

The data will be scraped from [11v11](https://www.11v11.com/) website. This will be cleaned, processed and visualised/analysed.

## Structure

### Code
The current structure of the code is as follows. 

```
📦code
 ┣ 📂Analysis
 ┃ ┗ 📜swansea_analysis.py
 ┣ 📂dashboard
 ┃ ┣ 📜app.py
 ┃ ┣ 📜app_tools.py
 ┃ ┗ 📜swansea_image.jpg
 ┣ 📂processing
 ┃ ┣ 📜process_swansea_city_all_matches.py
 ┃ ┗ 📜process_swansea_head_2_head.py
 ┣ 📂scraping
 ┃ ┣ 📜scrape_head_2_head.py
 ┃ ┣ 📜scrape_swansea_city_all_matches.py
 ┃ ┗ 📜__init__.py
 ┣ 📜config.ini
 ┣ 📜football_tools.py
 ┗ 📜__init__.py
```

### Data
The structure of the data is as follows:

```
📦data
 ┣ 📂head_2_head
 ┃ ┣ 📂BlackburnRovers
 ┃ ┃ ┗ 📜BlackburnRoversvSwanseaCity.csv
 ┃ ┗ 📂vBlackburnRover
 ┃ ┃ ┗ 📜SwanseaCityvBlackburnRovers.csv
 ┣ 📂raw
 ┃ ┣ 📜swanseacitymatches.txt
 ┃ ┗ 📜swanseacitymatches_jan2022.txt
 ┗ 📂transformed
 ┃ ┣ 📜swanseacitymatches.csv
 ┃ ┗ 📜swanseacitymatches_jan2022.csv
 ```
 
## Flow Diagram

Here is a flow diagram of what the process looks like: (TBD)


