import pandas

import mongoengine

db = pandas.read_csv("classes.csv")

unique = []
for i in db["Course title"]:
    if i not in unique:
        unique.append(i)
        print(i)
    else:
        pass