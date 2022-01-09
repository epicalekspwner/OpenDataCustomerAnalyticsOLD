# Connect Google Drive to Colab
from google.colab import drive
drive.mount('/content/drive')

# Import Pandas Library
import pandas as pd

# Import and Load Data Into DataFrames
df2016 = 'https://raw.githubusercontent.com/epicalekspwner/OpenData/main/popStructure/2016_popStructureAbsolute.csv'
df2017 = 'https://raw.githubusercontent.com/epicalekspwner/OpenData/main/popStructure/2017_popStructureAbsolute.csv'
df2018 = 'https://raw.githubusercontent.com/epicalekspwner/OpenData/main/popStructure/2018_popStructureAbsolute.csv'
df2019 = 'https://raw.githubusercontent.com/epicalekspwner/OpenData/main/popStructure/2019_popStructureAbsolute.csv'
df2020 = 'https://raw.githubusercontent.com/epicalekspwner/OpenData/main/popStructure/2020_popStructureAbsolute.csv'
list_dataset = [df2016, df2017, df2018, df2019, df2020]

# Get Column Names and Drop Useless Attribute
attr = list(df2016.columns)
attr.remove('region')

# Iteration and Convertion Into Percentage (Within Country)
for i in list_dataset:
  for j in attr:
    i[j] = round(i[j]/i[j][26], 4)

# Export Processed DataFrames
df2016.to_csv('/content/drive/MyDrive/Datasets/2016_popStructureCountryRelative.csv')
df2017.to_csv('/content/drive/MyDrive/Datasets/2017_popStructureCountryRelative.csv')
df2018.to_csv('/content/drive/MyDrive/Datasets/2018_popStructureCountryRelative.csv')
df2019.to_csv('/content/drive/MyDrive/Datasets/2019_popStructureCountryRelative.csv')
df2020.to_csv('/content/drive/MyDrive/Datasets/2020_popStructureCountryRelative.csv')