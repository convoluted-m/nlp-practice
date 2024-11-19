## Reading tabulat text data

## Load data in a csv format using Python’s built-in csv module
# with keyword ensures file is closed properly
# newline argument prevents problems with reading files (like newline in the middle in the string)
import csv
with open('sample.csv', newline='') as file:  
    data = file.read()
    print(data)

## Load  a csv file using the panads library
import pandas as pd
file = "./sample.csv" 
# Read into DataFrame
df= pd.read_csv(file)
print(df)

