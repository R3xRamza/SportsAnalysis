import pandas as pd
import json

with open("statsPage.json") as f:
    jobject = json.load(f)
#print(jobject)


cols = jobject["Date"]
del jobject["Date"]

df = pd.DataFrame.from_dict(jobject,orient="index",columns=cols)
print(df)

