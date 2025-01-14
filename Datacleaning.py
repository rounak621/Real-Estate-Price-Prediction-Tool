import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
matplotlib.rcParams["figure.figsize"] = (20,10)

df1=pd.read_csv(r"https://raw.githubusercontent.com/rounak621/Real-Estate-Price-Prediction-Tool/refs/heads/main/Bengaluru_House_Data.csv")
df1.head()

df1.shape
df1.groupby("area_type")["area_type"].count()

df2 = df1.drop(["area_type","society","balcony","availability"], axis=1)
df2.head()
df2.isnull().sum()
df3=df2.dropna()
df3.isnull().sum()
df3.shape

df3["size"].unique()

df3["bhk"] = df3["size"].apply(lambda x: int(x.split(" ")[0]))
df3.head()
df3["bhk"].unique()

df3[df3.bhk>20]
df3["total_sqft"].unique()

def is_float(x):
    try:
        float(x)
    except:
        return False
    return True
df3[~df3["total_sqft"].apply(is_float)].head(10)

def convert_sqft_to_num(x):
    tokens=x.split("-")
    if len(tokens)==2:
        return(float(tokens[0])+float(tokens[1]))/2
    try:
        return float(x)
    except:
        return None
df4=df3.copy()
df4["total_sqft"]=df4["total_sqft"].apply(convert_sqft_to_num)
df4.head()df4.loc[30]
df5=df4.copy()
df5["price_per_sqft"] = df5["price"]*100000/df5["total_sqft"]
df5.head()
df5.location.unique()
len(df5.location.unique())
df5.location=df5.location.apply(lambda x: x.strip())
location_stats=df5.groupby("location")["location"].agg("count").sort_values(ascending=False)
location_stats
len(location_stats[location_stats<=10])
location_stats_less_than_10 = (location_stats[location_stats<=10])
location_stats_less_than_10 
len(df5.location.unique())
df5["location"] = df5["location"].apply(lambda x: "other" if x in location_stats_less_than_10 else x)
len(df5.location.unique())
df5.head()
