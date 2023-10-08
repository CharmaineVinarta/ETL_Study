# Read CSV and JSON file types.
# Extract data from the above file types.
# Transform data.
# Save the transformed data in a ready-to-load format which data engineers can use to load into an RDBMS.

# import the required functions
import glob                           #helps to select files
import pandas as pd                   # helps to process csv files
import xml.etree.ElementTree as ET    # helps to process xml files
from datetime import datetime

# downloading the files using wget
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip

# unzip the files
!unzip source.zip

# set paths
tmpfile    = "temp.tmp"               # file used to store all extracted data
logfile    = "logfile.txt"            # all event logs will be stored in this file
targetfile = "transformed_data.csv"   # file where transformed data is stored

# from here, do the Extraction

# CSV Extraction Function
def extracted_from_csv(file_to_process):
  dataframe = pd.read_csv(file_to_process)
  return dataframe

# JSON Extraction Function
def extracted_from_json(file_to_process):
  dataframe = pd.read_json(file_to_process)
  return dataframe

# XML Extraction Function
def extracted_from_sml(file_to_process):
  dataframe = pd.DataFrame(columns=["name", "height", "weight"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        dataframe = dataframe.append({"name":name, "height":height, "weight":weight}, ignore_index=True)
    return dataframe

# Extract Function
# first, create an empty data frame to hold extracted data
def extract():
  extracted_data = pd.DataFRame(columns= ['name','height','weight'])  # create empty data frame

    #process all csv files
    for csvfile in glob.glob("*.csv"):
        extracted_data = extracted_data.append(extract_from_csv(csvfile), ignore_index=True)
        
    #process all json files
    for jsonfile in glob.glob("*.json"):
        extracted_data = extracted_data.append(extract_from_json(jsonfile), ignore_index=True)
    
    #process all xml files
    for xmlfile in glob.glob("*.xml"):
        extracted_data = extracted_data.append(extract_from_xml(xmlfile), ignore_index=True)
        
    return extracted_data

# Transform Function
def transform(data):
  data['height'] = round(data.height * 0.0254,2)
        #Convert height which is in inches to millimeter
        #Convert the datatype of the column into float
        #data.height = data.height.astype(float)
        #Convert inches to meters and round off to two decimals(one inch is 0.0254 meters)
  data['weight'] = round(data.weight * 0.45359237,2)
  return data
        #Convert weight which is in pounds to kilograms
        #Convert the datatype of the column into float
        #data.weight = data.weight.astype(float)
        #Convert pounds to kilograms and round off to two decimals(one pound is 0.45359237 kilograms)

# Loading Function
def load(targetfile,data_to_load):
  data_to_load.to_csv(targetfile)

# Logging function
def log(message):
  timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-monthname-day-hour-minute-second
  now = datetime.now() # get current timestamp
  timestamp = now.strftime(timestamp_format)
  with open("logfile.txt","a") as f:
      f.write(timestamp + ',' + message + '\n')

# Running ETL Process Functions
log ("ETL Job Started")

log("Extract phase Started")
extracted_data = extract()
log("Extract phase Ended")
extracted_data

log("Transform phase Started")
transformed_data = transform(extracted_data)
log("Transform phase Ended")
transformed_data

log("Load phase Started")
load(targetfile, transformed_data)
log("Load phase Ended")

log("ETL Job Ended")


