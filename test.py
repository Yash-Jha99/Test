import pandas as pd
import json

# read by default 1st sheet of an excel file
df = pd.read_excel("Equipments Mapping.xlsx", usecols=[0], sheet_name="BULL")

data = df.values.tolist()

list = []

category = data[1][0]
dat = {"category": category, "models": []}

for index, item in enumerate(data):
    if index == 0:
        continue

    print(index, data[index])
    if index == len(data) - 1:
        dat["models"].append(item[0])
        dat["models"].append("other")
        list.append(dat)
        break
    if item[0] == category:
        continue
    if type(item[0]) == float:
        if index > 1:
            dat["models"].append("other")
            list.append(dat)
            dat = {"category": "", "models": []}
        category = data[index + 1][0]
        dat["category"] = category
    else:
        dat["models"].append(item[0])

# del dat["nan"]

print(json.dumps(list))
