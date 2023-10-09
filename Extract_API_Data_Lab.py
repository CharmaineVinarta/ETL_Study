# Collect exchange rate data using an API
# Store the data as a CSV

# install libraries
#!mamba install pandas==1.3.3 -y
#!mamba install requests==2.26.0 -y
!mamba install bs4==4.10.0 -y
!mamba install html5lib==1.1 -y

from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd

# My access key
access_key = '7a212d3678e207a467dbb5a05c3ff195'

# Extract Data Using an API
# Extract currency exchange rate data using Exchangerate-API
# API KEY: 7a212d3678e207a467dbb5a05c3ff195

# Call the API
# Question 1 Using the requests library call the endpoint given above and save the text, remember the first few characters of the output:
# Write the code below
url = f"http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=7a212d3678e207a467dbb5a05c3ff195"
response = requests.get(url)
data = response.json()

# Save as DataFrame
# Question 2 Using the data gathered turn it into a pandas dataframe. 
# The dataframe should have the Currency as the index and Rate as their columns. Make sure to drop unnecessary columns.

# Turn the data into a dataframe
# Write the code below
df = pd.DataFrame(data.items(), columns=["Currency", "Rate"]).set_index("Currency")

# Load the Data
# Using the dataframe save it as a CSV names exchange_rates_1.csv.
# Save the Dataframe
# Write the code below
df.to_csv("exchange_rates_1.csv")
print(df)
