import os
import numpy as np
import pandas as pd
import random

data=[]
# create data
for _ in range(2500):
    math=random.randint(0,100)
    reading=random.randint(0,100)
    writing=random.randint(0,100)
    attendance=random.randint(0,100)
    homework=random.randint(0,100)

    avg=(math+reading+writing+attendance+homework)/5
    if avg>65:
        grade="A"
    elif avg>55:
        grade="B"
    elif avg>40:
        grade="C"
    else:
        grade="D"

    data.append([math, reading, writing,attendance, homework,grade])

df =pd.DataFrame(data,columns=["math","reading","writing","attendance","homework", "grade"])

# intentional addition of incorrect values
df.loc[167:183,"math"]=np.nan
df.loc[56:67,"writing"]=np.nan
df.loc[5, "attendance"] = 150
df.loc[234, "attendance"] = 111
df.loc[8, "reading"] = -20
df.loc[432, "reading"] = -60
df.loc[1, "grade"] = "a"
df.loc[78, "grade"] = "a"
df.loc[3, "grade"] = "bardzo dobry"
df.loc[56, "grade"] = "bardzo dobry"
df= pd.concat([df,df.iloc[45:48]])
df= pd.concat([df,df.iloc[237:241]])


CURRENT_DIR=os.path.dirname(os.path.abspath(__file__))
BASE_DIR=os.path.dirname(CURRENT_DIR)
DATA_DIR=os.path.join(BASE_DIR,"data")
csv_path=os.path.join(DATA_DIR,"raw_data.csv")

df.to_csv(csv_path, index=False)