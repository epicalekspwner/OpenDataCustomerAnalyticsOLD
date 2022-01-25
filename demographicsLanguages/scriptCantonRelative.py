# Connect Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Import Pandas Library
import pandas as pd

# Set Periodicity From 2016 to 2019
periodicity = range(2016,2020)

# Create New Dictionary
dictURL = {}

# Create Corresponding URLs and Store Them in the Dictionary Created Beforehand
for year in periodicity:
  dictURL['df_{0}'.format(year)] = 'https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsLanguages/' + str(year) + '_demographicsLanguagesAbsolute.csv'

# Get the Dictionary Keys to Access the URLs
keys = list(dictURL.keys())

# Create New Dictionary for Storing the DataFranes
dictDataFrames = {}

# Accessing the Original Datasets Through URLs and Converting Them Into DataFrames
for i in range(len(keys)):
  dictDataFrames['{0}'.format(keys[i])] = pd.read_csv(dictURL[keys[i]])

# Get Column Names and Drop Useless Attribute
attr = list(dictDataFrames[keys[0]].columns)
attr.remove('region')
attr.remove('total')
languageIC = ['german_IC','french_IC','italian_IC','romansh_IC','english_IC','portuguese_IC','serbianCroatian_IC','albanian_IC','spanish_IC','turkish_IC','otherLanguages_IC']
for i in languageIC:
  attr.remove(i)
  
# Iteration and Convertion Into Percentage (Within Canton)
for i in range(len(dictDataFrames)):
  for j in attr:
    dictDataFrames[keys[i]][j] = round(dictDataFrames[keys[i]][j]/dictDataFrames[keys[i]]['total'], 4)
  for i in range(len(dictDataFrames)):
    dictDataFrames[keys[i]]['total'] = round(dictDataFrames[keys[i]]['total']/dictDataFrames[keys[i]]['total'], 4)
    
# Export DataFrames
yearList = list(periodicity)
for i in range(len(dictDataFrames)):
  exportLink = '/content/drive/MyDrive/Datasets/{0}_demographicsLanguagesCantonRelative.csv'.format(yearList[i])
  dictDataFrames[keys[i]].to_csv(exportLink)