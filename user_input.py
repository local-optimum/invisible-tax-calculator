from datetime import date
import pandas as pd
import sys

#set today's month as the default end date to ensure the API call goes up to today
today_time = date.today().strftime("%Y-%m")


#import user transactions and convert to a dictionary
while True:
    try: 
        print("Please submit your deposits/withdrawls in the following format:\n2020-03 8000\n2019-04 7999\n2020-06 -5000\nDo not duplicate monthly entries or they will be overwritten.\nUse Ctril+d to submit your data without entering a blank line")
        userdepositraw = sys.stdin.read()
        deposits = dict(x.split() for x in userdepositraw.splitlines())
        for key in deposits:
            deposits[key] = int(deposits[key])
        print()
        print("Deposits submitted, thank you.")
        break
    except:
        print("Input not accepted, please try again.")
    

""" #create a dictionary of values
deposits = {}

#test dictionary for debugging
#deposits = {'2020-01': 4000, '2019-03': 40000, '2019-08': 7000}


#Legacy input code, replaced with improved ability to paste bulk inputs
additional_deposit_check = "y"

while additional_deposit_check == "y":
    
    key = input("Enter the deposit date in the format YYYY-MM: ")
    value = int(input("Enter the amount deposited in GBP: "))

    deposits[key]= value

    print("Your deposit history so far is:")
    print(deposits)

    additional_deposit_check = input("Do you want to track additional deposits? Y/n: ").lower() """




#find the earliest date to query inflation data from

date_list = list(deposits.keys())
earliest_date = sorted(date_list)[0]

start_time =earliest_date
end_time =today_time