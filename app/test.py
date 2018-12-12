import pandas

import mongoengine

db = pandas.read_csv("classes.csv")

for i in db["Course title"]:
    print(i)