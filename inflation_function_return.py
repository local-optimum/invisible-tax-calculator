from user_input import *
from api_cleanup import *
import pandas as pd


# insert deposit amounts at the corresponding date
deposit_df = pd.merge(monthly_infl_percentage,netdepositsdf, on = 'year_month', how='left')
deposit_df = deposit_df.fillna(0)
#Create calculatable columns
deposit_df["running_deposit_total"] = 0
deposit_df["inflation_compound_percentage_increase"] = 0
deposit_df["adjusted_total"] = 0


# calculcate running total column of desposits adjusted by inflation, adding new deposits but not adjusting them when deposited

for ind in deposit_df.index:
    if ind == 0:
        deposit_df.loc[ind, "adjusted_total"] = deposit_df.loc[ind, "deposits"]
        deposit_df.loc[ind,
                       "running_deposit_total"] = deposit_df.loc[ind, "deposits"]
        deposit_df.loc[ind, "inflation_compound_percentage_increase"] = 0
    else:
        deposit_df.loc[ind, "adjusted_total"] = round(
            (100/(deposit_df.loc[ind, "inflation_percentage_change"]+100)*deposit_df.loc[ind-1, "adjusted_total"])+deposit_df.loc[ind, "deposits"], 2)
        deposit_df.loc[ind, "running_deposit_total"] = deposit_df.loc[ind -
                                                                      1, "running_deposit_total"]+deposit_df.loc[ind, "deposits"]
        deposit_df.loc[ind, "inflation_compound_percentage_increase"] = round(
            (100+deposit_df.loc[ind-1, "inflation_compound_percentage_increase"])*((100+deposit_df.loc[ind, "inflation_percentage_change"])/100)-100, 2)
print("Desposit history table generated...")

# return final total

final_total = round(list(deposit_df["adjusted_total"])[-1], 2)
deposit_total = sum(deposit_df["deposits"])
inflation_tax = round(deposit_total-final_total, 2)
inflation_percentage = round(
    ((deposit_total-final_total)/deposit_total)*100, 2)
pp_total = round(deposit_total/(1-(inflation_percentage/100)), 2)

print("\n\nYour total deposits were: ", str(deposit_total), " GBP")
print("If held as cash, today your deposits would be worth: ",
      str(final_total), " GBP")
print("Your inflation tax amounts to: ", str(inflation_tax),
      " GBP or ", str(inflation_percentage), "%")
print("To retain your purchasing power you would need to hold: ",
      str(pp_total), " GBP")
