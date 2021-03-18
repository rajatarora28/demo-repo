#Import Modules
import pandas as pd
import requests
from pprint import pprint


#edit from VS code
#Read Data from csv
df = pd.read_csv("data.csv")


#Select only Name, Age and Gender
df = df[['name','age','gender']]