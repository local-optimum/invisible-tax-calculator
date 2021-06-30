from datetime import date
import pandas as pd

#set today's month as the default end date
today_time = date.today().strftime("%Y-%m")


#create a dictionary of values
deposits = {}

#test dictionary for debugging
#deposits = {'2020-01': 4000, '2019-03': 40000, '2019-08': 7000}

additional_deposit_check = "y"

while additional_deposit_check == "y":
    
    key = input("Enter the deposit date in the format YYYY-MM: ")
    value = int(input("Enter the amount deposited in GBP: "))

    deposits[key]= value

    print("Your deposit history so far is:")
    print(deposits)

    additional_deposit_check = input("Do you want to track additional deposits? Y/n: ").lower()




#find the earliest date to query inflation data from

date_list = list(deposits.keys())
earliest_date = sorted(date_list)[0]

print(earliest_date)

start_time =earliest_date
end_time =today_time