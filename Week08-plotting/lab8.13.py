#Mess around with real data
import os
import pandas as pd
import matplotlib.pyplot as plt


os.chdir(os.path.dirname(__file__)) # set os path to that of current directory 

filename = 'real_life_data.xlsx'

xls = pd.ExcelFile(filename)
df = pd.read_excel(xls, 'Sheet1')
print(df.head())


x = df['Date']
y = df['Drug Release']
#dataframe["Date"] = pd.to_datetime(dataframe["Date"], format="%Y")

plt.scatter(x,y)
plt.show()
