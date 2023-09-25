import pandas as pd
import json
from settings import DATAPATH as d

jobject = pd.read_json("NewstatsPage.json")
plSt = jobject["bos"]["jayson-tatum"]
cols = plSt["Date"]
del plSt["Date"]
for i,j in dict(plSt).items():
    if i[:3] not in ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]:
        del plSt[i]


df = pd.DataFrame.from_dict(plSt,orient="index",columns=cols)
#df["PTS"].astype(int)
print(df["PTS"].astype(int).sum())

# def seperateFG(val):
#     return val.split("-")[0]
# print(df["3PT"].transform(seperateFG))

# df["3PM"] = df["3PT"].transform(lambda val: val.split("-")[0])
# df["3PA"] = df["3PT"].transform(lambda val: val.split("-")[1])
# del df["3PT"]
# print(df)

# a = df.apply(lambda val: val.loc["3PT"].split("-"), axis=1)
# df["3PM"] = a.transform[0]
# df["3PA"] = a[1]
# print(df)


