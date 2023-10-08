# Use webscraping to get bank information

# install/import libraries 
#!mamba install pandas==1.3.3 -y
#!mamba install requests==2.26.0 -y
!mamba install bs4==4.10.0 -y
!mamba install html5lib==1.1 -y

from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd

# Extract Data Using Web Scraping
# The wikipedia webpage link:
# https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks provides information about largest banks in the world by various parameters. Scrape the data from the table 'By market capitalization' and store it in a JSON file.

# Webpage Contents
# Problem 1: Gather the contents of the webpage in text format using the requests library and assign it to the variable html_data

# Write your code here:
html_data = requests.get("https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks").text

html_data[760:783]

# Scraping the Data
# Problem 2 Using the contents and beautiful soup load the data from the By market capitalization table into a pandas dataframe. The dataframe should have the bank Name and Market Cap (US$ Billion) as column names. Display the first five rows using head.
# Using BeautifulSoup parse the contents of the webpage.

# Write your code here:
soup=BeautifulSoup(html_data, "html5lib")

# Load the data from the By market capitalization table into a pandas dataframe. 
# The dataframe should have the bank Name and Market Cap (US$ Billion) as column names. Using the empty dataframe data and the given loop extract the necessary data from each row and append it to the empty dataframe.
# Problem 3, filling the write you code here.

data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

for row in soup.find_all('tbody')[2].find_all('tr'):
    col = row.find_all('td')
    #Write your code here:
    if len(col) >= 2:
        name = col[0].get_text(strip=True)
        market_cap = col[1].get_text(strip=True)
        data = data.append({"Name": name, "Market Cap (US$ Billion)": market_cap}, ignore_index=True)

# Problem 4, Display the first five rows using the head function.
# Write your code here: 
print(data.head())

# Loading the Data
# Load the pandas dataframe created above into a JSON named bank_market_cap.json using the to_json() function.
# Problem 5, Write your code here:
data.to_json("bank_market_cap.json")
