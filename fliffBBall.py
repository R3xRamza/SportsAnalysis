import pandas as pd
import json
from settings import DATAPATH as d

jobject = pd.read_json("NewstatsPage.json")


dL = dict(jobject)

# for i,j in dL.items():
#     print(i+":")
#     for x,y in j.items():
#         print(x+":")
#         if y:
#             cols = y["Date"]
#             del y["Date"]
#             b = dict(y)
#             for a,b in b.items():
#                 if a[:3] not in ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]:
#                     del y[a]

plSt = jobject["dal"]["luka-doncic"]

cols = plSt["Date"]
del plSt["Date"]
for i,j in dict(plSt).items():
    if i[:3] not in ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]:
        del plSt[i]

def first5(pl):
    pl = dict(list(pl.items())[:5])
    f5 = pd.DataFrame.from_dict(pl,orient="index",columns=cols)
    print(f5)
 


df = pd.DataFrame.from_dict(plSt,orient="index",columns=cols)
print(df)
first5(plSt)
