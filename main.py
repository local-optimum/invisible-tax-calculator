#for graphing the output
import pylab as plt


#intro text
print("\n\n\nWelcome to Local Optimum's Inflation Calculator!")
print("First we'll create a dictionary of deposit dates and amounts.")
print("Negative deposits can be used to represent withdrawls.")
print("Only submit *net* deposits per date.")

#create dictionary of deposits
import user_input

print("\nThis tool uses monthly percentage change to inflation in the UK across the whole CPI.")
print("source: https://stats.oecd.org/Index.aspx?DataSetCode=PRICES_CPI#")


#use API to pull monthly inflation history from OECD based on earliest deposit date
import api_cleanup


#combine the deposts dictionary and api stats to create an adjusted running total
from inflation_function_return import *

#graphing section
print("generating graph")
print("Once the graph has been closed you will be prompted to save the raw data as table if preferred.")
plt.figure("infoutput")
plt.clf()
plt.plot(deposit_df["year_month"], deposit_df["running_deposit_total"], label="Balance Total")
plt.plot(deposit_df["year_month"], deposit_df["adjusted_total"], label="Value_Total")
plt.title("Deposit Value Decay")
plt.ylim(bottom=0)
plt.xticks([])
plt.show()


#optonal export for personal analysis
while True:
    df_dump_check =input("\nWould you like to export your monthly change to csv? Y/n: ").lower()
    if df_dump_check == 'y' or df_dump_check =='n':
        break
    else:
        print('Input not recognised.')

if df_dump_check == "y":
    name =str(input("Please name your output: "))
    deposit_df.to_csv(name+".csv", encoding="utf-8") 
    print(f"Your CSV has been saved to the project folder as '{name}.csv'.")

print("Thank you for testing Local Optimum's inflation tracker, feel free to leave feedback on github!\n\n\n")
#complete