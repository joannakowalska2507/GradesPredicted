import pandas as pd
import numpy as np
import os

CURRENT_DIR=os.path.dirname(os.path.abspath(__file__))
BASE_DIR=os.path.dirname(CURRENT_DIR)
DATA_DIR=os.path.join(BASE_DIR,"data")
csv_path=os.path.join(DATA_DIR,"raw_data.csv")

df=pd.read_csv(csv_path)

#checking for empty values and completing them
print(df.isna().sum())
df["math"]=df["math"].fillna(df["math"].median())
df["writing"]=df["writing"].fillna(df["writing"].median())

#removing duplicates
print(df.duplicated().sum())
df=df.drop_duplicates()

#out-of-range value improvement
print(df.describe())
df["reading"]=df["reading"].clip(lower=0)
df["attendance"]=df["attendance"].clip(upper=100)

#type validation
print(df.dtypes)

#checking category consistency
print(df["grade"].value_counts())
df["grade"] = df["grade"].replace({
    "bardzo dobry": "A"
})
df["grade"] = df["grade"].str.upper()

print(df.info())
csv_path=os.path.join(DATA_DIR,"clean_data.csv")
df.to_csv(csv_path,index=False)