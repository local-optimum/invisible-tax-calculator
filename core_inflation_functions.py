
import requests
import json

#https://stats.oecd.org/restsdmx/sdmx.ashx/GetDataStructure/PRICES_CPI

response = requests.get("https://stats.oecd.org/SDMX-JSON/data/PRICES_CPI/GBR.CPALTT01.IXOB+IXOBSA+GY+GP+IXNB+AL+CTGY.M/all?startTime=2021-01&endTime=2021-05")
print(response.status_code)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

python_obj = response.json()["dataSets"][0]["series"]["0:0:0:0"]["observations"]

jprint(python_obj)

values = python_obj.values()
values_list = list(values)

inf_stats = []

for i in values_list:
    inf_stats.append(i[0])

print(inf_stats)


