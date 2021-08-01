import pandas as pd

#functions

def depcheck(df,dict):
    """Function that takes a data frame and a dictionary 
    and uses the key of the dictionary to add values into 
    the dataframe at the matching index"""
    for key in dict:
        df.loc[key,"deposits"] = dict[key]
    return df

#import dataframe of inflation percentages over time
from api_cleanup import monthly_infl_percentage
from user_input import deposits

#debug dataframe
#monthly_infl_percentage = pd.DataFrame({"year_month": ["2021-01","2021-02","2021-03"], "inflation_percentage_change": [0.1,0.5,-0.1]})
#monthly_infl_percentage = monthly_infl_percentage.set_index("year_month")
#deposits = {"2021-01":100,"2021-03":500}



#add column of deposits and corresponding to date rows
monthly_infl_percentage["deposits"] = 0

#to track running total of desposits to create a graph
monthly_infl_percentage["running_deposit_total"]=0
monthly_infl_percentage["inflation_compound_percentage_increase"]=0


#insert deposit amounts at the corresponding date
deposit_df = depcheck(monthly_infl_percentage,deposits)
deposit_df.reset_index(inplace = True)

#calculcate running total column of desposits adjusted by inflation, adding new deposits but not adjusting them when deposited
deposit_df["adjusted_total"] = 0

for ind in deposit_df.index:
    if ind == 0:
        deposit_df.loc[ind, "adjusted_total"] = deposit_df.loc[ind,"deposits"]
        deposit_df.loc[ind, "running_deposit_total"] = deposit_df.loc[ind,"deposits"]
        deposit_df.loc[ind, "inflation_compound_percentage_increase"] = 0
    else:
        deposit_df.loc[ind, "adjusted_total"] = round((100/(deposit_df.loc[ind,"inflation_percentage_change"]+100)*deposit_df.loc[ind-1,"adjusted_total"])+deposit_df.loc[ind,"deposits"],2)
        deposit_df.loc[ind, "running_deposit_total"] = deposit_df.loc[ind-1, "running_deposit_total"]+deposit_df.loc[ind,"deposits"]
        deposit_df.loc[ind, "inflation_compound_percentage_increase"] = round((100+deposit_df.loc[ind-1, "inflation_compound_percentage_increase"])*((100+deposit_df.loc[ind,"inflation_percentage_change"])/100)-100,2)
print("Desposit history table generated...")

#return final total

final_total = round(list(deposit_df["adjusted_total"])[-1],2)
deposit_total = sum(deposit_df["deposits"])
inflation_tax = round(deposit_total-final_total,2)
inflation_percentage = round(((deposit_total-final_total)/deposit_total)*100,2)
pp_total = round(deposit_total/(1-(inflation_percentage/100)),2)

print("\n\nYour total deposits were: ", str(deposit_total)," GBP")
print("If held as cash, today your deposits would be worth: ", str(final_total)," GBP")
print("Your inflation tax amounts to: ", str(inflation_tax), " GBP or ", str(inflation_percentage),"%")
print("To retain your purchasing power you would need to hold: ", str(pp_total)," GBP")