

print("Welcome to Local Optimum's Inflation Calculator!")
print("First we'll create a dictionary of deposit dates and amounts.")

#create dictionary of deposits
import user_input

print("This tool uses monthly percentage change to inflation in the UK across the whole CPI.")
print("source: https://stats.oecd.org/Index.aspx?DataSetCode=PRICES_CPI#")


#use API to pull monthyl inflation history from OECD based on earliest deposit date
import api_cleanup


#combine the deposts dictionary and api stats to create an adjusted running total
import inflation_function_return

#complete