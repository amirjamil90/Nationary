# Demo for the working of Python Pandas on Excel Column names
# Location of the Building Code shall be fetched from 2 columns i.e. Latitude and Longitude.
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('nation.xlsx', sheet_name='Sheet1',sep='\s*,\s*')

print("Column headings:")
a=df['LATITUDE'].tolist()
b=df['LONGITUDE'].tolist()

for i in range(0,len(a)):
	print(a[i])
	print(b[i])

