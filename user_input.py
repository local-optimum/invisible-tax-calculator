from datetime import date
import pandas as pd
import sys

#set today's month as the default end date to ensure the API call goes up to today
today_time = date.today().strftime("%Y-%m")


#import user transactions and convert to a dataframe
while True:
    try: 
        print("Please submit your deposits/withdrawls in the following format:\nYYYY-MM XXXX\nYYYY-MM XXXX\nUse Ctril+d to submit your data without entering a blank line")
        userdepositraw = sys.stdin.read().splitlines()
        deposits = [x.split() for x in userdepositraw]
        depositsdf = pd.DataFrame(deposits, columns = ['year_month','deposits'])
        depositsdf['deposits']= depositsdf['deposits'].astype(int)
        depositsdf['year_month'] = pd.to_datetime(depositsdf['year_month'])
        netdepositsdf = depositsdf.groupby(['year_month']).sum().reset_index()
        print()
        print("Deposits submitted, thank you.")
        break
    except:
        print("Input not accepted, please try again.")

#find the earliest date to query inflation data from

earliest_date = min(netdepositsdf['year_month'])

start_time =earliest_date.strftime("%Y-%m")
end_time =today_time