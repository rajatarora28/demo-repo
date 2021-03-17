#First Part
import pandas as pd
import requests
from pprint import pprint

print("Libraries Imported...")


#Second Part
df = pd.read_csv("data.csv")



#Third Part
df = df[['Name','Age','Sex']]
