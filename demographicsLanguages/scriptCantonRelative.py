# Connect Google Drive to Colab
from google.colab import drive
drive.mount('/content/drive')

# Import Pandas Library
import pandas as pd

# Import, Load Data Into DataFrames & Replace 'XXX' With Actual Token
df2016 = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsLanguages/2016_demographicsLanguagesAbsolute.csv?token=XXX')
df2017 = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsLanguages/2017_demographicsLanguagesAbsolute.csv?token=XXX')
df2018 = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsLanguages/2018_demographicsLanguagesAbsolute.csv?token=XXX')
df2019 = pd.read_csv('https://raw.githubusercontent.com/epicalekspwner/OpenDataCustomerAnalytics/main/demographicsLanguages/2019_demographicsLanguagesAbsolute.csv?token=XXX')
list_dataset = [df2016, df2017, df2018, df2019]

# Get Column Names and Drop Useless Attribute
attr = list(df2016.columns)
attr.remove('region')
attr.remove('total')
languageIC = ['germanIC','frenchIC','italianIC','romanshIC','englishIC','portugueseIC','serbian&croatianIC','albanianIC','spanishIC','turkishIC','otherLanguagesIC']
for i in languageIC:
  attr.remove(i)

# Iteration and Convertion Into Percentage (Within Canton)
for i in list_dataset:
  for j in attr:
    i[j] = round(i[j]/i['total'], 4)
for i in list_dataset:
  i['total'] = round(i['total']/i['total'], 4)
  
# Export Processed DataFrames
df2016.to_csv('/content/drive/MyDrive/Datasets/2016_demographicsLanguagesCantonRelative.csv')
df2017.to_csv('/content/drive/MyDrive/Datasets/2017_demographicsLanguagesCantonRelative.csv')
df2018.to_csv('/content/drive/MyDrive/Datasets/2018_demographicsLanguagesCantonRelative.csv')
df2019.to_csv('/content/drive/MyDrive/Datasets/2019_demographicsLanguagesCantonRelative.csv')
