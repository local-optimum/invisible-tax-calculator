# Local Optimum's Inflation Tax Calculator

## What is it and what does it do?
The inflation tax calculator enables users to enter deposit dates (in YYYY-MM format) and GBP amounts to create a dictionary of historical deposits.
This dictionary is used to query the OECD website's historical CPI monthly inflation change for the UK.
This is then used to create a table of running monthly totals modified by the monthly percentage change.
The output consists of:
* The total amount deposited
* The current value of this amount if held as cash
* The total and percentage decrease in value
* How much cash you would need to hold to retain your purchasing power

You can optionally export the full table to csv for your own analysis or reference (eg to make a graph of value over time).

## Why did I make it?
This is my first independent project that did not follow a tutorial or guide. 
It was designed to help my consider how best to structure my code and how best to present it to a public audience.
It also answered a question I was personally interested in addressing.
If anyone is interested in giving me feedback on my approach or structure I would be happy to hear it.


## What do I need to run it?
This code can be run in the terminal by running main.py from the project folder.
It requires only a few basic libraries to run:
* Pandas
* Requests
* Json
* Datetime
* Matplotlib

The data is pulled from this OECD site
https://stats.oecd.org/Index.aspx?DataSetCode=PRICES_CPI#