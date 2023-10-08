# import functions

import glob                        #to help selecting file
import pandas as pd                #to import csv file
import xml.etree.ElementTree as ET #to import xml file
from datetime import datetime      

# download file
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/datasource.zip
# data was saved to datasource.zip

# since the dl file was zip, we need to unzip it using !unzip
!unzip datasource.zip -d dealership_data

# !unzip: This is the command to unzip a compressed archive. 
# The exclamation mark (!) is often used in command-line interfaces to execute a command.
# datasource.zip: This is the name of the ZIP file that you want to unzip.
# -d: This is a flag that indicates you are specifying a destination directory for the extracted files and folders.
# dealership_data: This is the directory where you want to extract the contents of datasource.zip. 
# In other words, after running this command, the files and folders from datasource.zip will be extracted into the dealership_data directory.

# set path
tmpfile    = "dealership_temp.tmp"              # used to store all extracted data
logfile    = "dealership_logfile.txt"           # all events will be stored here
targetfile = "dealership_transformed_data.csv"  # transformed data will be stored here

# Extract Function
### Question 1: CSV Extract Function

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe
  
### Question 2: JSON Extract Function

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe
  
### Question 3: XML Extract Function

def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        car_model = person.find("car_model").text
        year_of_manufacture = int(person.find("year_of_manufacture").text)
        price = float(person.find("price").text)
        fuel = person.find("fuel").text
        dataframe = dataframe.append({"car_model":car_model, "year_of_manufacture":year_of_manufacture, "price":price, "fuel":fuel}, ignore_index=True)
    return dataframe

### Question 4: Extract Function 
### (Call the specific extract functions by replacing the ADD_FUNCTION_CALL with the proper function call)

def extract():
    extracted_data = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])
### processing all csv file
    for csvfile in glob.glob("dealership_data/*.csv"):
      extracted_data = extracted_data.append("ADD_FUNCTION_CALL",ignore_index=True)
### processing all json file
    from jsonfile in glob.glob("dealership_data/*.json"):
      extracted_data = extracted_data.append("ADD_FUNCTION_CALL",ignore_index=True)
### processing all xml file
    from xmlfile in glob.glob("dealership_data/*.csv"):
      extracted_data = extracted_data.append("ADD_FUNCTION_CALL",ignore_index=True)
    return extracted_data
  
### Question 5: Transform
def transform(data):
    data["price"] = round(data.price, 2)
    return data

### Question 6: Load
def load(targetfile,data_to_load):
    data_to_load.to_csv(targetfile)  

### Question 7: Log
def log(message):
    timestamp_format = '%H:%M:%S-%h-%d-%Y' #Hour-Minute-Second-MonthName-Day-Year
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("dealership_logfile.txt","a") as f:
        f.write(timestamp + ',' + message + '\n') 

### Question 8: ETL Process
log("ETL Job Started")

log("Extract phase Started")
extracted_data = extract()
log("Extract phase Ended")

log("Transform phase Started")
transformed_data = transform(extracted_data)
log("Transform phase Ended")

log("Load phase Started")
load(targetfile,transformed_data)
log("Load phase Ended")

log("ETL Job Ended")


