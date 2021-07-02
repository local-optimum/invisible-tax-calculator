
import requests
import json
from datetime import date
import pandas as pd

#https://stats.oecd.org/restsdmx/sdmx.ashx/GetDataStructure/PRICES_CPI


#bring in start and end times from user input
from user_input import *


#debugging start and end times while building user_input
#start_time ="2019-01"
#end_time ="2021-07"
today_time = date.today().strftime("%Y-%m")
measure_param="GP"

#function for analysing api query, used for debugging
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


#input date parameters to api

parameters = {
    "startTime": start_time,"endTime": end_time

}

#get api
response = requests.get("https://stats.oecd.org/SDMX-JSON/data/PRICES_CPI/GBR.CPALTT01.GP.M/all", params=parameters)

#select inflation stats from the dataset & convert into list
inf_obj = response.json()["dataSets"][0]["series"]["0:0:0:0"]["observations"]

inf_list = list(inf_obj.values())

inf_stats = [d[0] for d in inf_list]

#select matching dates from the dataset & convert into list
date_obj = response.json()["structure"]["dimensions"]["observation"][0]["values"]

date_stats = [d["id"] for d in date_obj]

#combine dates and stats into a dataframe for analysis
monthly_infl_percentage = pd.DataFrame({"year_month": date_stats, "inflation_percentage_change": inf_stats})
monthly_infl_percentage = monthly_infl_percentage.set_index("year_month")
