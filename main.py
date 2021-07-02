

print("Welcome to Local Optimum's Inflation Calculator!")
print("First we'll create a dictionary of deposit dates and amounts.")
print("You can include negative deposits to represent withdrawls, but please only submit *net* deposits per date.")

#create dictionary of deposits
import user_input

print("This tool uses monthly percentage change to inflation in the UK across the whole CPI.")
print("source: https://stats.oecd.org/Index.aspx?DataSetCode=PRICES_CPI#")


#use API to pull monthyl inflation history from OECD based on earliest deposit date
import api_cleanup


#combine the deposts dictionary and api stats to create an adjusted running total
from inflation_function_return import *

df_dump_check =input("Would you like to export your monthly change to csv? Y/n: ").lower()

if df_dump_check == "y":
    deposit_df.to_csv("personalised_inflation_tracker.csv", encoding="utf-8") 
    print("Your CSV has been saved to the project folder as 'personalised_inflation_tracker.csv'.")

print("Thank you for testing Local Optimum's inflation tracker, feel free to leave feedback on github!")

#complete